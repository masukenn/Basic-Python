W, H, x, y, r = map(int, input().split())
if r <= x and x <= (W-r) and r <= y and y <= (H-r):
    print("Yes")
else:
    print("No")