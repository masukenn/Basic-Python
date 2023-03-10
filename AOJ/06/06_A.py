n = int(input())
number = list(map(int, input().split()))
number.reverse()
print(*number)