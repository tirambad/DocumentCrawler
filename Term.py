__author__ = 'tirambad'
class Term:
    # Actual Term
    term_str = ''
    # Number of document containing the term
    doc_frequency = 0
    # List containing the documents which contains the term
    #doc_list=[]
    # Each Term overall Stat example 'word' => [3,[doc_1,doc_1_freq],[doc_2,doc_2_freq],[doc_2,doc_2_freq]]
    term_stat=[]

    def __init__(self, str):
        self.term_str = str
        self.term_stat=[]


    def increase_frequency(self):
        self.doc_frequency += 1

    def add_doc_stat(self,doc_id,doc_freq):
        doc_list = []
        doc_list.append(doc_id)
        doc_list.append(doc_freq)
        self.term_stat.append(doc_list)
        #print(doc_list)
        #print(self.term_stat)
        # print('In Term Str='+self.term_str)
        # print('In term stat =' +str(self.term_stat))

    def get_term(self):
        return self.term_str

    def get_frequency(self):
        return self.doc_frequency

    def get_list(self):
        #print(self.term_stat)
        return self.term_stat
