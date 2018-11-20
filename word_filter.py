class WordFilter:

    def __init__(self, ng_word, replace_word="<censored>"):
        self.ng_word = ng_word
        self.replace_word = replace_word

    def detect(self, texts):
        return self.ng_word in texts

    def censor(self, texts):
        if self.detect(texts):
            return texts.replace(self.ng_word, self.replace_word)
        return texts
