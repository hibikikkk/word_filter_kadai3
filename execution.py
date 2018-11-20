from word_filter import WordFilter

if __name__ == "__main__":
    my_filter = WordFilter("アーセナル")

    print(my_filter.detect("昨日のアーセナルの試合アツかった！"))

    print(my_filter.detect("昨日のリバプールの試合アツかった！"))
