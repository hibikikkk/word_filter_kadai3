class WordFilter:

    def __init__(self, ng_words=[], replace_word="<censored>"):
        self.ng_words = ng_words
        self.replace_word = replace_word

    def detect(self, texts, ng_word_index=0):
        return self.ng_words[ng_word_index] in texts

    def censor(self, texts, ng_word_index):
        if self.detect(texts, ng_word_index):
            texts = texts.replace(self.ng_words[ng_word_index], self.replace_word)

        return texts

    def all_censor(self, texts):
        for counter in range(len(self.ng_words)):
            texts = self.censor(texts=texts, ng_word_index=counter)

        return texts


    def convert_ng_word(self):
        self.show_ng_words()
        convert_index = int(input("何番のNGワードを変えますか？ > "))
        after_word = input("変更後のワードを入力してください > ")

        # 空文字列なら変更しない
        if after_word != "":
            self.ng_words[convert_index] = after_word

    def show_ng_words(self):
        counter = 0
        for word in self.ng_words:
            print(f"{counter}: {word}")
            counter += 1
