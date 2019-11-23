import random
import matplotlib.pyplot as plt
import sys
from player import Player
from player import Robot
from population import Population

def one_run(population, iterations, hasRobots):
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
        if hasRobots and t>= (iterations-nmedia):
            m = population.media()
            mediap += m[0]
            mediaq += m[1]
        #m=population.media()  
        #mediasp+=[m[0]]
        #mediasq+=[m[1]]
        if t>=(iterations-100) and not hasRobots:
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
    if not hasRobots:
        return (mediap/(100),mediaq/(100))
    else:
        return (mediap / (nmedia), mediaq / (nmedia))

def main(argv):
    n=101
    e=0.001
    iterations=800000
	#Robot Variation
    if (len(argv) > 1 and argv[1] == '-r'):
        print("Robot Variation")
        hasRobots = True
        neighborIterations = 30
        robots = int(argv[0])
        neighbors = 4
        sub = "_robot"
	#Standard
    else:
        hasRobots = False
        neighborIterations=1
        neighbors = int(argv[0])
        sub = ""
    pm=0
    qm=0
    for i in range(neighborIterations):
        if hasRobots:
            print(str(robots)+ "->" + str(i))
        else:
            print(str(neighbors)+"->"+str(i))
        population=Population(n,e)
        #make_graph(population)
        #print(population.media())
        if hasRobots:
            for i in range(robots):
                population.addRobot(random.random(), random.random())
        population.createNetworkRing(neighbors)
        t=one_run(population,iterations, hasRobots)
        pm+=t[0]
        qm+=t[1]
    pm/=neighborIterations
    qm/=neighborIterations
    nomeFicheiro='neighbor_run_'+ argv[0] + sub
    f=open(nomeFicheiro,'w')
    conteudo=str(pm)+" "+str(qm)
    f.write(conteudo)
    f.close()
    if hasRobots:
        print(str(robots) + " acabou")
    else:
        print(str(neighbors)+" acabou")
    
if __name__== "__main__":
    main(sys.argv[1:])
