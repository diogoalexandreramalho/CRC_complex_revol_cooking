import random
import matplotlib.pyplot as plt
import sys,getopt
from player import Player
from player import Robot
from population import Population

def one_run(population, iterations, neighborIterations):
    mediasp=[]
    mediasq=[]
    mediap=0
    mediaq=0
    varp=[100,-1]
    varq=[100,-1]
    nmedia=100000
    
    for t in range(iterations):
        p1=population.randomPlayer()
        p2=population.randomNeighbor(p1)
        f1=population.getFitness(p1)
        f2=population.getFitness(p2)
        if f2>f1:
            population.imitate(p1,p2)
        if neighborIterations==1:
            m=population.media()  
            mediasp+=[m[0]]
            mediasq+=[m[1]]
            if t>= (iterations-nmedia):
                mediap += m[0]
                mediaq += m[1]
                varp[0]=min(varp[0],m[0])
                varp[1]=max(varp[1],m[0])
                varq[0]=min(varq[0],m[1])
                varq[1]=max(varq[1],m[1])
        else:
            if t>= (iterations-nmedia):
                m=population.media()  
                mediap += m[0]
                mediaq += m[1]
                varp[0]=min(varp[0],m[0])
                varp[1]=max(varp[1],m[0])
                varq[0]=min(varq[0],m[1])
                varq[1]=max(varq[1],m[1])
                
    if neighborIterations==1:
        plt.subplot(2, 1, 1)
        plt.scatter(list(range(len(mediasp))),mediasp)
        plt.title('Ps')
        plt.subplot(2, 1, 2)
        plt.scatter(list(range(len(mediasq))),mediasq,c='orange')
        plt.title('Qs')
        plt.show()
    return [[mediap/nmedia,varp[0],varp[1]],[mediaq/nmedia,varq[0],varq[1]]]

def main(argv):
    n=101
    e=0.001
    iterations=800000
    robots = 0
    neighbors= 4
    neighborIterations=30
    try:
        opts,args = getopt.getopt(argv,"n:r:i:e:")
    except getopt.GetoptError:
        print('test.py -n <neighbors> -r <robots> -i <iterations>')
        sys.exit(2)
    for opt, arg in opts:
        if opt=="-n":
            neighbors = int(arg)
        elif opt=="-r":
            robots = int(arg)
        elif opt=="-i":
            neighborIterations=int(arg)
        elif opt=="-e":
            e=float(arg)
    pm=0
    qm=0
    varp=[100,-1]
    varq=[100,-1]
    for i in range(neighborIterations):
        print(str(robots)+","+str(neighbors)+","+str(e) + "->" + str(i))
        population=Population(n,e)
        for i in range(robots):
            population.addRobot(random.random(), random.random())
        population.createNetworkRing(neighbors)
        t=one_run(population,iterations,neighborIterations)
        pm+=t[0][0]
        qm+=t[1][0]
        if t[0][1]<varp[0]:
            varp[0]=t[0][1]
        if t[0][2]>varp[1]:
            varp[1]=t[0][2]
        if t[1][1]<varq[0]:
            varq[0]=t[1][1]
        if t[1][2]>varq[1]:
            varq[1]=t[1][2]
    pm/=neighborIterations
    qm/=neighborIterations
    nomeFicheiro='ring_run_'+ str(robots) + "_robots_"+str(neighbors)+"_neighbors_"+str(e)+"_epsilon"
    f=open(nomeFicheiro,'w')
    conteudo=str(pm)+" "+str(qm)+" "+str(varp[0])+" "+str(varp[1])+" "+str(varq[0])+" "+str(varq[1])
    f.write(conteudo)
    f.close()
    print(str(robots)+","+str(neighbors) + " acabou")
    
if __name__== "__main__":
    main(sys.argv[1:])
