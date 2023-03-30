while True:
    x = int(input())
    if x == 0:
        break
    a = str(x)
    a_list = list(a)
    b_list = [int(i) for i in a_list]
    total = sum(b_list) 
    print(total)

