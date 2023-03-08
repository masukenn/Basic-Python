a, b = map(int, input().split())
d = a // b
r = a % b
f = a / b
print('{} {} {:.10f}'.format(d, r, f))