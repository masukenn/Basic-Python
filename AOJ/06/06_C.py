n = int(input())                                                            
list = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]   #多次元配列の生成
c = 0
while c != n:
    b, f, r, v = map(int, input().split())
    list[b-1][f-1][r-1] += v
    c += 1

for b in range(4):
    for f in list[b]:
         print('',*f)                                                   #[]と,の削除
    if b != 3:
        print("#"*20)
