class Dice:

#初期値
    def __init__(self, saikoro1):
        self.top = saikoro1[0]
        self.south = saikoro1[1]
        self.east = saikoro1[2]
        self.west = saikoro1[3]
        self.north = saikoro1[4]
        self.bottom = saikoro1[5]
#回転 
    def E(self):
        self.top, self.east, self.bottom, self.west = self.west, self.top, self.east, self.bottom
    
    def N(self):
        self.top, self.north, self.bottom, self.south = self.south, self.top, self.north, self.bottom

    def S(self):
        self.top, self.north, self.bottom, self.south = self.north, self.bottom, self.south, self.top
    
    def W(self):
        self.top, self.east, self.bottom, self.west = self.east, self.bottom, self.west, self.top

#判定
    def hanntei(self, saikoro2):
        for _ in range(4):
            self.N()
            for _ in range(4):
                self.E()
                for _ in range(4):
                    self.S()
                    for _ in range(4):
                        self.W()
                        if self.top == saikoro2[0] and self.south == saikoro2[1] and self.east == saikoro2[2] and self.west == saikoro2[3] and self.north == saikoro2[4] and self.bottom == saikoro2[5]:
                            return True
                        else:
                            continue


A = Dice(list(map(int, input().split())))
B = list(map(int, input().split()))
if A.hanntei(B) == True:
    print('Yes')
else:
    print('No')




        
