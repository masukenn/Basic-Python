while True:
    x = int(input())
    if x ==0:
        break
    a = str(x)
    b = list(a)                     #文字列をリストに
    int_list = [int(i) for i in b]   #リストの方変更：要素だけ取り出して型変換
    answer = sum(int_list)
    print(answer)

