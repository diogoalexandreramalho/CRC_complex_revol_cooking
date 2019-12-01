import random
import matplotlib.pyplot as plt
import sys
from player import Player
from population import Population

def one_run(population,iterations):
    m=population.media()
    n=len(population.population)
    mediasp=[]
    mediasq=[]
    mediap=0
    mediaq=0
    fitness=[]
    for t in range(iterations):
        flag=False
        p1=population.randomPlayer()
        p2=population.randomNeighbor(p1)
        f1=population.getFitness(p1)
        f2=population.getFitness(p2)
        if f2>f1 and not p1.isRobot:
            previous=(p1.p,p1.q)
            population.imitate(p1,p2)
            flag=True
        if flag:
            m=(m[0]-previous[0]+p1.p,m[1]-previous[1]+p1.q)   
        mediasp+=[m[0]/n]
        mediasq+=[m[1]/n]
        if t>=(iterations-1000):
            mediap+=m[0]/n
            mediaq+=m[1]/n

    plt.subplot(2, 1, 1)
    plt.plot(list(range(len(mediasp))),mediasp)
    plt.title('Ps')
    plt.subplot(2, 1, 2)
    plt.plot(list(range(len(mediasq))),mediasq,c='orange')
    plt.title('Qs')
    plt.show()
    plt.show()
    return (mediap/1000,mediaq/1000)

def main():
    n=20
    e=0.001
    iterations=1000000
    neighborIterations=1
    pm=0
    qm=0
    for i in range(neighborIterations):
        population=Population(n*n,e)
        #make_graph(population)
        #print(population.media())
        population.createNetworkGrid(n)
        t=one_run(population,iterations)
        pm+=t[0]
        qm+=t[1]
    pm/=neighborIterations
    qm/=neighborIterations
    print(pm," ",qm)
    
if __name__== "__main__":
    main()
