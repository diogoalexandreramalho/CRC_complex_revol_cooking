import random

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
    def getFitness(self):
        for i in self.neighbors:
            play

def createGeneration(n):
    population=[]
    for i in range(n):
        population+=[Player()]
    return population

def createNetworkRing(population,number):
    for i in range(len(population)):
        for n in range(-number//2,number//2+1):
            if n!=0:
                population[i].neighbors+=[(i+n)%len(population)]

def getFitness(player,population):
    fitness=0
    for i in player.neighbors:
        fitness+=player.play(population[i])
    return fitness

def imitate(p1,p2,population,e):
    error=random.random()*2*e
    p1.p=p2.p+(error-e)
    p1.q=p2.q+(error-e)
    if p1.p>1:
        p1.p=1
    elif p1.p<0:
        p1.p=0
    if p1.q>1:
        p1.q=1
    elif p1.q<0:
        p1.q=0

def media(population):
    p=0
    q=0
    for i in population:
        p+=i.p
        q+=i.q
    return (p/len(population),q/(len(population)))


def main():
    e=0.001
    population=createGeneration(100)
    print(media(population))
    createNetworkRing(population,4)
    for i in range(1000000):
        p1=random.choice(population)
        p2=population[p1.chooseRandomNeighbor()]
        f1=getFitness(p1,population)
        f2=getFitness(p2,population)
        if f2>f1:
            imitate(p1,p2,population,e)
    print(media(population))


if __name__== "__main__":
  main()