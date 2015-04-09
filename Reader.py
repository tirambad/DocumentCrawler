__author__ = 'tirambad'
import os
import PorterStemmer
import sys
from collections import Counter
import re
import Dictionary
import Term
import datetime

dictionary =Dictionary.Dictionary()

def printDocDetails(iterat,doc_id):
    iterat.sort()
    #uniqueCount=len(set(iterat))
    counts=Counter(iterat)
    counts=sorted(counts.items())
    #line=str(counts[1])
    #line=re.sub('(),','',line);
    #line=line.replace(',\',','');
    '''
    if(doc_id==1):
        f=open('Resources/results.txt','w')
    else:
        f=open('Resources/results.txt','a')
    #fwriteLn=''
    '''
    for i in range(len(counts)):
        line=str(counts[i])

        line=line.replace('(','')
        line=line.replace(')','')
        line=line.replace('\'','')
        line=line.replace(',','')
        split_w = re.split(' ', line)
        term_str=split_w[0]
        term_count = int(split_w[1])
        already_present=False
        term_obj=dictionary.return_term(term_str)
        if(term_obj == None):
            term_obj = Term.Term(term_str)
        else:
            already_present=True
            #key_term=dictionary.return_key(term_str)
        '''
        if(dictionary.isPresent(term_str)):
            term_obj=dictionary.return_term(term_str)
            already_present=True
            key_term=dictionary.return_key(term_str)
        else:
            term_obj = Term.Term(term_str)
        '''
        #print("Term :"+term_str +" doc_id: "+ str(doc_id)+" term count :"+str(term_count))
        term_obj.add_doc_stat(doc_id,term_count)
        term_obj.increase_frequency()
        if(already_present):
            dictionary.update_term(term_str,term_obj)
        else:
            dictionary.addTerm(term_str,term_obj)
        #writeLn=str(doc_id)+' '+ str(uniqueCount)+' '+ line
        #print(term_obj.get_term() + ' ' + str(term_obj.get_frequency()) + ' ' +str(term_obj.get_list()))
        #if(isPresent):

        # print(writeLn)
        #fwriteLn=fwriteLn+writeLn +'\n'
        #print(dictionary.list_items())
    #f.write(fwriteLn)



origFile = []
stopFile = []
start_time=datetime.datetime.now()
print("Opening Source File")
origf='Resources/cran.all.1400'
#origf='Resources/test.txt'
print("Opening StopWords File")
stopf = 'Resources/stopwords.txt'
#dictionary = Dictionary()
doc_id=term=0
stop_f=open(stopf,'r')
word=''
print('Creating Stop File Word List')
for line in stop_f:
    for c in line:
        if c!='\n':
            word += c.lower()
        else:
            stopFile.append(word)
            word=''
stopFile.append('')
stop_f.close()

port = PorterStemmer.PorterStemmer();
prev='False'
orig_f=open(origf,'r')
word=''
#Stem the word using porter Stemmer
print('Applying Porter Stemmer and creating the source file word list')
for line in orig_f:
    for c in line:
        if (c != ' ' and c != '\n'):
            word += c.lower()
        else:
            word=port.stem(word, 0,len(word)-1)
            if(word!='.t' and word!='.b' and word!='.a' and word!='.w'):
                if(word[-1:]=='.'):
                    word=word[:-1]
                origFile.append(word)
            word=''
#origFile.sort()
orig_f.close()

#Original File = Original File - Stop words
print('Removing Stop Words List from the Source List')
origFile=[x for x in origFile if x not in stopFile]
#print(len(origFile))
#print('unique count: '+ str(len(set(origFile))))
prevWord=''
doc_id=0
iterator =[]
appCheck=True
"""
Go through the originalFile-Step File
If the current word is .i, Print the Document Deatails and reset the iterator, update the Doc_ID
"""

print('Creating Dictionary')
for i in range(len(origFile)):
    if(origFile[i]=='.i'):
        if(len(iterator)>0):
            printDocDetails(iterator,doc_id)
            iterator=[]
        doc_id=int(origFile[i+1])
        appCheck=False
    else:
        if(appCheck):
            if '-' in origFile[i]:
                splitted=str(origFile[i]).split('-')
                for j in range(len(splitted)):
                     iterator.append(splitted[j])
            iterator.append(origFile[i])
        else:
            appCheck=True;
printDocDetails(iterator,doc_id)
print('Dictionary Creation Completed')

#print(dictionary.list_items())
print('Hashing Initiated')
dictionary.write_inverse_file()
end_time=datetime.datetime.now()
execution_time=end_time-start_time
#dictionary
print('Hashing Done')
print('Total Time of Execution = '+str(execution_time.seconds) + ' seconds')
print('Hash File is located in Resources/InverseHashFile.txt')






#print(port.stem('testing', 0,len('testing')-1))


#print ('test: '+str(len(sys.argv)))



#print(origFile)

