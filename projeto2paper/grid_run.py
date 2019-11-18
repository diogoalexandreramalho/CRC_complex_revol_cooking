import random
import matplotlib.pyplot as plt
import sys
from player import Player
from population import Population

def one_run(population,iterations):
    mediasp=[]
    mediasq=[]
    mediap=0
    mediaq=0
    for t in range(iterations):
        p1=population.randomPlayer()
        p2=population.randomNeighbor(p1)
        f1=population.getFitness(p1)
        f2=population.getFitness(p2)
        if f2>f1:
            population.imitate(p1,p2) 
        m=population.media()   
        mediasp+=[m[0]]
        mediasq+=[m[1]]
        if t>=(iterations-100):
            mediap+=m[0]
            mediaq+=m[1]
    
    #make_graph(population)
    plt.scatter(list(range(len(mediasp))),mediasp)
    plt.show()
    return (mediap/(100),mediaq/(100))

def main():
    n=20
    e=0.001
    iterations=2*800000
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
