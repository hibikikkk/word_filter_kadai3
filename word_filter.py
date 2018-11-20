class WordFilter:

    def __init__(self, ng_word):
        self.ng_word = ng_word

    def detect(self, texts):
        return self.ng_word in texts
