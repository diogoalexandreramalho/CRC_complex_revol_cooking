import random
import matplotlib.pyplot as plt
import sys
from player import Player
from population import Population
from player import Robot
def one_run(population,iterations):
    mediasp=[]
    mediasq=[]
    mediap=0
    mediaq=0
    nmedia=100000
    for t in range(iterations):
        p1=population.randomPlayer()
        p2=population.randomNeighbor(p1)
        f1=population.getFitness(p1)
        f2=population.getFitness(p2)
        if f2>f1:
            population.imitate(p1,p2)   
        if t>=(iterations-nmedia):
            m=population.media() 
            mediap+=m[0]
            mediaq+=m[1]
        '''m=population.media() 
        mediasp+=[m[0]]
        mediasq+=[m[1]]
        if t%100000==0:
            population.make_graph()
    plt.subplot(2, 1, 1)
    plt.scatter(list(range(len(mediasp))),mediasp)
    plt.title('Ps')
    plt.subplot(2, 1, 2)
    plt.scatter(list(range(len(mediasq))),mediasq,c='orange')
    plt.title('Qs')
    plt.show()'''
    return (mediap/(nmedia),mediaq/(nmedia))

def main(argv):
    n=101
    e=0.001
    iterations=800000
    neighborIterations=30
    pm=0
    qm=0
    robots=int(argv[0])
    neighbors=4
   
    for i in range(neighborIterations):
        print(str(robots)+"->"+str(i))
        population=Population(n,e)
        for i in range(robots):
            population.addRobot(random.random(),random.random())
        population.createNetworkRing(neighbors)
        t=one_run(population,iterations)
        pm+=t[0]
        qm+=t[1]
    #population.make_graph()
    pm/=neighborIterations
    qm/=neighborIterations
    nomeFicheiro='robot_run_'+argv[0]
    f=open(nomeFicheiro,'w')
    conteudo=str(pm)+" "+str(qm)
    f.write(conteudo)
    f.close()
    print(str(robots)+" acabou")
    
if __name__== "__main__":
    main(sys.argv[1:])