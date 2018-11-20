class WordFilter:

    def __init__(self, ng_words=[], replace_word="<censored>"):
        self.ng_words = ng_words
        self.replace_word = replace_word

    def detect(self, texts, ng_word_counter=0):
        return self.ng_words[ng_word_counter] in texts

    def censor(self, texts, counter):
        if self.detect(texts, counter):
            texts = texts.replace(self.ng_words[counter], self.replace_word)

        return texts

    def all_censor(self, texts):
        for counter in range(len(self.ng_words)):
            texts = self.censor(texts=texts, counter=counter)

        return texts


    def convert_ng_word(self):
        self.show_ng_words()
        convert_number = int(input("何番のNGワードを変えますか？ > "))
        after_word = input("変更後のワードを入力してください > ")

        # 空文字列なら変更しない
        if after_word != "":
            self.ng_words[convert_number] = after_word

    def show_ng_words(self):
        counter = 0
        for word in self.ng_words:
            print(f"{counter}: {word}")
            counter += 1
