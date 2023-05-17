while True:
    x, y = map(int, input().split())
    if (x,y) == (0,0):
        break
    elif x < y:
        print(x, y)
    else:
        print(y, x)
