class Dice:
    def __init__(self, saikoro):
        self.saikoro = saikoro

    def E(self):
        self.saikoro[0], self.saikoro[2], self.saikoro[5], self.saikoro[3] = self.saikoro[3], self.saikoro[0], self.saikoro[2], self.saikoro[5]
    
    def N(self):
        self.saikoro[0], self.saikoro[1], self.saikoro[5], self.saikoro[4] = self.saikoro[1], self.saikoro[5], self.saikoro[4], self.saikoro[0]

    def S(self):
        self.saikoro[0], self.saikoro[1], self.saikoro[5], self.saikoro[4] = self.saikoro[4], self.saikoro[0], self.saikoro[1], self.saikoro[5]
    
    def W(self):
        self.saikoro[0], self.saikoro[2], self.saikoro[5], self.saikoro[3] = self.saikoro[2], self.saikoro[5], self.saikoro[3], self.saikoro[0]

    def top(self):
        print(self.saikoro[0])
    
A = Dice(input().split())
x = input()
for i in x:
    if i == 'E':
        A.E()
    if i == 'N':
        A.N()
    if i == 'S':
        A.S()
    if i == 'W':
        A.W()
A.top()

#classの使い方。　初期情報も入る。
#selfで特定できる。

        
    

