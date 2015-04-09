__author__ = 'tirambad'
import Dictionary
import re
import Term
from collections import Counter
dict1=dict()
dict1={1:'test1'}
dict1.update({2:'test2'})
#print('Dict Get Values '+str(dict1.get(2)))
print(dict1)
print(dict1.items())
diction = Dictionary.Dictionary();
if 'test1' in dict1.values():
        print("Print key is here")
else:
    print("HEHE")

test_token = '575 126 affect 1'
# test =[]
term_o = Term.Term('Tirambad')

diction.addTerm('Tirambad',term_o)
#print('Key is : ' + str(diction.return_key('Tirambad')))
term_o2=Term.Term('test')
diction.addTerm('test',term_o2)
print('Dict Get Values '+str(diction.get_term('Tirambad')))

#print('Key is : ' + str(diction.return_key('test')))
#print(diction.list_items())
'''
test = re.split(' ',test_token)
print(test)
print(test[0])
dictionary=Dictionary
'''