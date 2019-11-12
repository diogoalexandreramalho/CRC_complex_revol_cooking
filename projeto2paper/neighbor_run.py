import random
import matplotlib.pyplot as plt
import sys
class Player:
    def __init__(self):
        self.p=random.random()
        self.q=random.random()
        self.neighbors=[]
    def play(self,s2):
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
        self.q=p2.q+(error-e)
        if self.p>1:
            self.p=1
        elif self.p<0:
            self.p=0
        if self.q>1:
            self.q=1
        elif self.q<0:
            self.q=0

class Population:
    def __init__(self,n,e):
        self.population=[]
        self.e=e
        for i in range(n):
            self.population+=[Player()]

    def createNetworkRing(self,number):
        for i in range(len(self.population)):
            for n in range(-number//2,number//2+1):
                if n!=0:
                    self.population[i].neighbors+=[(i+n)%len(self.population)]

    def getFitness(self,player):
        fitness=0
        for i in player.neighbors:
            fitness+=player.play(self.population[i])
        return fitness
    
    def media(self):
        p=0
        q=0
        for i in self.population:
            p+=i.p
            q+=i.q
        return (p/len(self.population),q/(len(self.population)))

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

def one_run(population,iterations):
    mediasp=[]
    mediasq=[]
    iterations=800000
    mediap=0
    mediaq=0
    for t in range(iterations):
        p1=population.randomPlayer()
        p2=population.randomNeighbor(p1)
        f1=population.getFitness(p1)
        f2=population.getFitness(p2)
        if f2>f1:
            population.imitate(p1,p2)    
        #mediasp+=[m[0]]
        #mediasq+=[m[1]]
        if t>=(iterations-100):
            m=population.media()
            mediap+=m[0]
            mediaq+=m[1]
    
    #make_graph(population)
    #plt.scatter(list(range(len(mediasp))),mediasp)
    #plt.show()
    return (mediap/(100),mediaq/(100))

def main(argv):
    n=100
    e=0.001
    iterations=800000
    neighborIterations=30
    pm=0
    qm=0
    neighbors=int(argv[0])
    for i in range(neighborIterations):
        print(str(neighbors)+"->"+str(i))
        population=Population(100,0.001)
        #make_graph(population)
        #print(population.media())
        population.createNetworkRing(neighbors)
        t=one_run(population,iterations)
        pm+=t[0]
        qm+=t[1]
    pm/=neighborIterations
    qm/=neighborIterations
    nomeFicheiro='neighbor_run_'+argv[0]
    f=open(nomeFicheiro,'w')
    conteudo=str(pm)+" "+str(qm)
    f.write(conteudo)
    f.close()
    print(str(neighbors)+" acabou")
    
if __name__== "__main__":
    main(sys.argv[1:])