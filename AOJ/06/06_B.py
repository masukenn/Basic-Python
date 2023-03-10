n = int(input())
allcard = list()   
patern = ['S', 'H', 'C', 'D']
for egara2 in patern:
    for suuji2 in range(1 , 14):
        allcard.append(egara2 + ' ' + str(suuji2))

for data in range(n):
    egara, suuji = input().split()
    allcard.remove(egara + ' ' + str(suuji))

for i in range(len(allcard)):
    print(allcard[i])


    