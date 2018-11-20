from word_filter import WordFilter

if __name__ == "__main__":
    input_replace_word = input("置き換える文字列はなんですか？ > ")

    if input_replace_word != "":
        my_filter = WordFilter("アーセナル", input_replace_word)

    if input_replace_word == "":
        my_filter = WordFilter("アーセナル")

    # print(my_filter.detect("昨日のアーセナルの試合アツかった！"))
    #
    # print(my_filter.detect("昨日のリバプールの試合アツかった！"))

    print(my_filter.censor("昨日のアーセナルの試合アツかった！"))
    print(my_filter.censor("昨日のリバプールの試合アツかった！"))
