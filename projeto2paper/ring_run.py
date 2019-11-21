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
        #m=population.media()  
        #mediasp+=[m[0]]
        #mediasq+=[m[1]]
        if t>=(iterations-100):
            m=population.media()
            mediap+=m[0]
            mediaq+=m[1]
    
    #make_graph(population)
    '''plt.subplot(2, 1, 1)
    plt.scatter(list(range(len(mediasp))),mediasp)
    plt.title('Ps')
    plt.subplot(2, 1, 2)
    plt.scatter(list(range(len(mediasq))),mediasq,c='orange')
    plt.title('Qs')
    plt.show()'''
    return (mediap/(100),mediaq/(100))

def main(argv):
    n=101
    e=0.001
    iterations=800000
    neighborIterations=1
    pm=0
    qm=0
    neighbors=int(argv[0])
    for i in range(neighborIterations):
        print(str(neighbors)+"->"+str(i))
        population=Population(n,e)
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
