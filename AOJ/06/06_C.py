n = int(input())                                                            
building = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(4)]  # 多次元配列の生成
c = 0
while c != n:
    b, f, r, v = map(int, input().split())
    building[b-1][f-1][r-1] += v
    c += 1
for b in range(4):
    for f in building[b]:
        print(*f)
    if b != 3:
        print("#"*20)
