import random

class Player:
    def __init__(self,p=-1,q=-1):
        self.p=p
        self.q=q
        self.isRobot=False
        if self.p==-1:
            self.p=random.random()
            self.q=random.random()
        self.neighbors=[]
    def play(self,s2):
        if s2.isRobot==True:
            s2.p=random.random()
            s2.q=random.random()
        payOff=0
        if self.p>=s2.q:
            payOff+=1-self.p
        if s2.p>=self.q:
            payOff+=s2.p
        return payOff
    def chooseRandomNeighbor(self):
        return random.choice(self.neighbors)
    def imitate(self,p2,e):
        error=random.random()*2*e
        self.p=p2.p+(error-e)
        error=random.random()*2*e
        self.q=p2.q+(error-e)
        if self.p>1:
            self.p=1
        elif self.p<0:
            self.p=0
        if self.q>1:
            self.q=1
        elif self.q<0:
            self.q=0


class Robot(Player):
    def __init__(self,p=-1,q=-1):
        super().__init__(p,q)
        self.isRobot=True
    def imitate(self,s2,e):
        return