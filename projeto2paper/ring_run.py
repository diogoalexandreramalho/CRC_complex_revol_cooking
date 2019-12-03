import random
import matplotlib.pyplot as plt
import sys,getopt
from player import Player
from player import Robot
from population import Population

def one_run(population, iterations, neighborIterations):
    m=population.media()
    n=len(population.population)-population.nrobots
    mediasp=[]
    mediasq=[]
    mediap=0
    mediaq=0
    varp=0
    varq=0
    nmedia=100000
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
        if t>=(iterations-nmedia):
            mediap += m[0]/n
            mediaq += m[1]/n
    mediap=mediap/nmedia
    mediaq=mediaq/nmedia
    c=[[0,0],[0,0]]
    for i in range(iterations-nmedia,iterations):
        varp+=(mediasp[i]-mediap)**2
        if mediasp[i]<mediap:
            c[0][0]+=1
        else:
            c[0][1]+=1
        varq+=(mediasq[i]-mediaq)**2
        if mediasq[i]<mediaq:
            c[1][0]+=1
        else:
            c[1][1]+=1
    varp/=(nmedia)
    varq/=(nmedia)
    varp=varp**0.5
    varq=varq**0.5
    if neighborIterations==1:
        plt.subplot(2, 1, 1)
        plt.plot(list(range(len(mediasp))),mediasp)
        plt.title('Ps')
        plt.subplot(2, 1, 2)
        plt.plot(list(range(len(mediasq))),mediasq,c='orange')
        plt.title('Qs')
        plt.show()
    return [[mediap,mediap-(varp*c[0][0]/(c[0][0]+c[0][1])),mediap+(varp*c[0][1]/(c[0][0]+c[0][1]))],
    [mediaq,mediaq-(varq*c[1][0]/(c[1][0]+c[1][1])),mediaq+(varq*c[1][1]/(c[1][0]+c[1][1]))]]

def main(argv):
    n=100
    e=0.001
    iterations=800000
    robots = 0
    neighbors= 4
    neighborIterations=30
    try:
        opts,args = getopt.getopt(argv,"n:r:i:e:p:")
    except getopt.GetoptError:
        print('test.py -n <neighbors> -r <robots> -i <iterations> -e <epsilon> -p population')
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
        elif opt=="-p":
            n=int(arg)
            iterations=8000000
    pm=0
    qm=0
    varp=[0,0]
    varq=[0,0]
    for i in range(neighborIterations):
        print(str(n)+","+str(robots)+","+str(neighbors)+","+str(e) + "->" + str(i))
        population=Population(n,e)
        for i in range(robots):
            population.addRobot(random.random(), random.random())
        population.createNetworkRing(neighbors)
        t=one_run(population,iterations,neighborIterations)
        pm+=t[0][0]
        qm+=t[1][0]
        varp[0]+=t[0][1]
        varp[1]+=t[0][2]
        varq[0]+=t[1][1]
        varq[1]+=t[1][2]
    varp[0]/=neighborIterations
    varp[1]/=neighborIterations
    varq[0]/=neighborIterations
    varq[1]/=neighborIterations
    pm/=neighborIterations
    qm/=neighborIterations
    nomeFicheiro='ring_run_'+str(n)+'_population_'+str(robots) + "_robots_"+str(neighbors)+"_neighbors_"+str(e)+"_epsilon"
    f=open(nomeFicheiro,'w')
    conteudo=str(pm)+" "+str(qm)+" "+str(varp[0])+" "+str(varp[1])+" "+str(varq[0])+" "+str(varq[1])
    f.write(conteudo)
    f.close()
    print(str(n)+","+str(robots)+","+str(neighbors)+","+str(e)+" acabou")
    
if __name__== "__main__":
    main(sys.argv[1:])
