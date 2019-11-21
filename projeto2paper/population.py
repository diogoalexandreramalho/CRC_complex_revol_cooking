from player import Player
from player import Robot
import random
import matplotlib.pyplot as plt
class Population:
    def __init__(self,n,e):
        self.population=[]
        self.e=e
        for i in range(n):
            self.population+=[Player()]

    def addPlayer(self,p,q):
        self.population+=[Player(p,q)]

    def addRobot(self,p,q):
        self.population[int(random.random()*len(self.population))]=Robot(p,q)

    def createNetworkRing(self,number):
        for i in range(len(self.population)):
            for n in range(-number//2,number//2+1):
                if n!=0:
                    self.population[i].neighbors+=[(i+n)%len(self.population)]

    def createNetworkGrid(self,n):
        for i in range(n):
            for j in range(n):
                node=i*n+j
                up=(node-n)%(n*n)
                down=(node+n)%(n*n)
                right=i*n+(j+1)%n
                left=i*n+(j-1)%n
                self.population[node].neighbors+=[up,right,down,left]
                

    def getFitness(self,player):
        fitness=0
        for i in player.neighbors:
            fitness+=player.play(self.population[i])
        return fitness
    
    def media(self):
        p=0
        q=0
        c=0
        for i in self.population:
            if i.isRobot==False:
                p+=i.p
                q+=i.q
                c+=1
        return (p/c,q/c)

    def make_graph(self):
        ps=[]
        qs=[]
        for i in self.population:
            ps+=[i.p]
            qs+=[i.q]
        plt.subplot(2, 1, 1)
        plt.scatter(list(range(1,len(self.population)+1)),ps,c='blue')
        plt.title('Ps')
        plt.subplot(2, 1, 2)
        plt.scatter(list(range(1,len(self.population)+1)),qs,c='orange')
        plt.title('Qs')
        plt.show()

    def randomPlayer(self):
        return random.choice(self.population)
    
    def randomNeighbor(self,player):
        return self.population[random.choice(player.neighbors)]

    def imitate(self,p1,p2):
        p1.imitate(p2,self.e)