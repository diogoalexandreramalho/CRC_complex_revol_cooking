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
        #if t%2000==0:
            #population.make_graph()
    #make_graph(population)
    plt.scatter(list(range(len(mediasp))),mediasp)
    plt.show()
    return (mediap/(100),mediaq/(100))

def main(argv):
    n=100
    e=0.001
    iterations=800000
    neighborIterations=1
    pm=0
    qm=0
    neighbors=int(argv[0])
    S1=(0.1,0.05)
    S2=(0.34,0.15)
    population=Population(0,e)

    for i in range(n-1):
        population.addPlayer(S1[0],S1[1])
    population.addPlayer(S2[0],S2[1])
    for i in range(neighborIterations):
        #make_graph(population)
        #print(population.media())
        population.createNetworkRing(neighbors)
        t=one_run(population,iterations)
        pm+=t[0]
        qm+=t[1]
    pm/=neighborIterations
    qm/=neighborIterations
    '''
    nomeFicheiro='neighbor_run_'+argv[0]
    f=open(nomeFicheiro,'w')
    conteudo=str(pm)+" "+str(qm)
    f.write(conteudo)
    f.close()'''
    print(str(neighbors)+" acabou")
    
if __name__== "__main__":
    main(sys.argv[1:])