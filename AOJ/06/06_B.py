n = int(input())
allcard = []  
patern = ['S', 'H', 'C', 'D']
allcard = [f'{egara2} {suuji2}' for egara2 in patern for suuji2 in range(1, 14)]            #内包型
for data in range(n):
    allcard.remove(input())

for card in allcard:#forのリスト参照
    print(card)