a, b, c = map(int, input().split())
x = 0
for data in range(a, b+1):
    if c % data == 0:
        x += 1
print(x)
