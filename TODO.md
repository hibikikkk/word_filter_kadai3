TODO
------------------

- [x] C-1:　NGワードが含まれているかどうかを判定できる
- [x] NGワードが含まれているかどうかを判定できる detect() メソッドを持つ WordFilterクラス を実装
    - [x] my_filter = WordFilter("アーセナル")
​
- [x] NGワードが含まれている場合 
    - [x] my_filter.detect("昨日のアーセナルの試合アツかった！") # Trueを返す 
​
- [x] NGワードが含まれていない場合 
    - [x] my_filter.detect("昨日のリバプールの試合アツかった！") # Falseを返す 



- [x] C-2:  NGワードを変換できる 
- [x] NGワードが含まれていた場合に、NGワードを <censored> という文字に変換できる censor メソッドを実装
    - [x] my_filter = WordFilter("アーセナル")
​
- [x] NGワードが含まれている場合 
    - [x] my_filter.censor("昨日のアーセナルの試合アツかった！") # "昨日の<censored>の試合アツかった！" を返す 
​
- [x] NGワードが含まれていない場合 
    - [x] my_filter.censor("昨日のリバプールの試合アツかった！") # "昨日のリバプールの試合アツかった！" を返す


```
応用問題
```
- [x] <censored> を自由に変更できるようにする
    - [x] NGワードが含まれていた場合に置き換える文字列を自由に設定できる

- [x] NGワードの複数登録
    - [x] NGワード"ガナーズ"も登録して変わっているか確認

- [x] NGワードの変更
    - [x] NGワード"アーセナル"を"ガナーズ"に変更して変わっているか確認