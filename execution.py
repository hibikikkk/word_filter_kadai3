from word_filter import WordFilter

if __name__ == "__main__":
    # 複数のNGワードを保存するためのリスト型変数
    ng_word_list = []

    # NGワードを入力するためのループ
    while True:
        ng_word_list.append(input("NGワードを入力してください >"))

        if input("NGワードは他にありますか？(はい or いいえ) >") == "いいえ":
            break

    # 置き換える文字列の入力
    input_replace_word = input("置き換える文字列はなんですか？ > ")

    # 置き換える文字列が文字列をWordFilterクラスに空文字でないなら保存する
    if input_replace_word != "":
        my_filter = WordFilter(ng_words=ng_word_list, replace_word=input_replace_word)

    if input_replace_word == "":
        my_filter = WordFilter(ng_words=ng_word_list)

    # 動作が行えているか確認用ループ
    while True:
        print(my_filter.all_censor("昨日のアーセナルとリバプールの試合アツかった！"))
        print(my_filter.all_censor("昨日のリバプールの試合アツかった！"))

        # NGワードの変更をする
        my_filter.convert_ng_word()
