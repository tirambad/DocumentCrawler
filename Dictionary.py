__author__ = 'tirambad'
import Term;
class Dictionary:
    #dictionary=None
    #termID=None

    def __init__(self):
        self.termID=0
        self.dictionary=dict()
        self.create_file=True
        #print('Dictionary Initiate'+str(self.dictionary))


    def addTerm(self,term_str,term):
        #print(self.termID)
        #print(term.get_term())
        self.termID+=1
        if(term_str != ''):
            self.dictionary[term_str]=term
        #self.termID += 1

    def update_term(self,key_term,term):
        self.dictionary[key_term]=term

    '''
    def isPresent(self,term):
        for termT in self.dictionary.values():
            #print(termT.get_term()+'='+term)
            if(termT.get_term() == term):
                return True
        return False
    '''
    def return_term(self,term):
        termT=self.dictionary.get(term)
        return  termT
        '''
        for termT in self.dictionary.values():
            if(termT.get_term() == term):
                return termT
        return None
        '''

    def list_items(self):
        #print(self.dictionary.items())
        for keyT,termT in self.dictionary.items():
            print(termT.get_term() + ' '+str(termT.get_frequency())+ ' '+str(termT.get_list()) + "key ="+str(self.termID) +'Term is:'+termT.get_term())


    '''
    def return_key(self,term):
        for keyT,termT in self.dictionary.items():
            #print(termT.get_term()+'='+term)
            #print('Dictioray is'+str(self.dictionary))
            #print('Term in dictionary is '+termT.get_term())
            #print('Key of Term is '+str(keyT))
            if(termT.get_term() == term):
                return keyT
        return False
        #return None
    '''

    def write_inverse_file(self):
        final_str=''
        for keyT,termT in self.dictionary.items():
            item_list=[]
            term_str="'"+termT.get_term()+"' => "
            item_list.append(termT.get_frequency())
            item_list.append(termT.get_list())
            final_str += term_str+(str(item_list)+'\n')
            if(self.create_file):
                f=open('Resources/InverseHashFile.txt','w')
                self.create_file=False
            else:
                f=open('Resources/InverseHashFile.txt','a')
        f.write(final_str)





