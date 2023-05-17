import sys

x = sys.stdin.read()
y = x.lower()
x_list = list(y)
alphabets = [0 for _ in range(26)]
for i in x_list:
    for j in range(26):
        if ord(i) == 97+j:
            alphabets[j] += 1

for j in range(26):
    print('{} : {}'.format(chr(97+j), alphabets[j]))

#asciiコード,uppper lower
#sys ctrl+z





