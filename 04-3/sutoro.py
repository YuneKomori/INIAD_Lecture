# 課題4-3-4. 文字列・ストロー関数
# 1. ストロー関数(「す」取ろう) sutoro (text) を作ってください。
# ■ 「す」取ろう関数は、引数に与えられた文字列 text の中から、「す」を取り除いた文字列を戻り値として 返します。
# ■ sutoro(text) 関数を用いて、次のプログラムを実行すると動作例のように実行されます。
# print(sutoro("さしすせそ"))
# 動作例:
# さしせそ
# 2. 次のスライドのプログラムを追記して、sutoro(text) 関数が正しい結 果となるか確認してみてください。
# 3. 完成したプログラム sutoro.py を提出してください。
text = """すぱいすそんつすかいこすなすすしてえすらいす
すそのちょすうしですこすれからすもすとりすくすもう
すこすこからすまたどすんどすんすむずすかしくす
なするすからすふくすしゃすうをすしっかすりすやすろうすね"""



# test="あいうえかきっけこ"
# for i in test:
#     print(i)


def sutoro(text):
    list=""
    for i in text:
        if i =="す":
            pass
        else:
            list+=i
    return list
    
        
print(sutoro(text))