while True:
    n, x = map(int, input().split())
    c = 0
    if n == 0 and x == 0:
        break
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i + j + k + 3 == x and i != j != k and i < j < k:
                    c += 1

    print(c)

    

