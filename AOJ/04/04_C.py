while True:
    a,op,b = input().split()
    a = int(a)
    b = int(b)
    if op == "?":
        break
    elif op =="+":
        ans = a + b
    elif op =="-":
        ans = a - b
    elif op =="*":
        ans = a * b
    elif op =="/":
        ans = a // b

    print(ans)