from .code import read_words, get_random_word, one_iteration

class OutputFromService:
    potential_words = None
    doc_name = None
    discarded = None
    confirmed = None
    yellow = None
    session_begin = None
    suggested_word = None
    interpreted_word = None


    def initialize_session(self):
        self.session_begin = True
        self.potential_words = read_words()
        self.discarded = []
        self.confirmed = {}
        self.yellow = {}
        self.doc_name = 'potential_words_1'
        self.suggested_word = ""
        self.interpreted_word = ""


    def get_suggested_word(self):
        self.suggested_word = get_random_word(self.potential_words)
        print("Suggested word is ",self.suggested_word)
        return self.suggested_word


    def set_result_from_game(self, interpreted_word):
        self.interpreted_word = interpreted_word
        self.interpret_word(self)


    def interpret_word(self):
        result = one_iteration(interpreted_word = self.interpreted_word, potential_words=self.potential_words, suggested_word=self.suggested_word, doc_name=self.doc_name, discarded=self.discarded, confirmed=self.confirmed, yellow=self.yellow)
        if len(result)>1:
            self.potential_words = result[0]
            self.doc_name = result[1]
            self.discarded = result[2]
            self.confirmed = result[3]
            self.yellow = result[4]
            # print("The guessed word "+result[0])
        else:
            print("word found")
            self.close_session(self)

    
    def close_session(self):
        self.session_begin = False
        self.potential_words = read_words()
        self.discarded = []
        self.confirmed = {}
        self.yellow = {}
        self.doc_name = 'potential_words_1'
        self.suggested_word = ""
        self.interpreted_word = ""


    
