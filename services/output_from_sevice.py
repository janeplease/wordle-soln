from code import get_word, read_words, get_random_word

class OutputFromService:
    potential_words = None
    doc_name = None
    discarded = None
    confirmed = None
    yellow = None
    session_begin = None


    def initialize_session(self):
        self.session_begin = True
        self.potential_words = read_words()
        self.discarded = []
        self.confirmed = {}
        self.yellow = {}
        self.doc_name = 'potential_words_1'


    def func(self):
        for i in range(6):
            suggested_word = get_random_word(self.potential_words)
            print(suggested_word)
            result = get_word(potential_words=self.potential_words, suggested_word=suggested_word, doc_name=self.doc_name, discarded=self.discarded, confirmed=self.confirmed, yellow=self.yellow)
            if len(result)>1:
                self.potential_words = result[1]
                self.doc_name = result[2]
                self.discarded = result[3]
                self.confirmed = result[4]
                self.yellow = result[5]
                print("The guessed word "+result[0])
            else:
                print("word found ")
                break

    
