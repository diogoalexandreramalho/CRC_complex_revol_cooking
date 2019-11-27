import random
import pylab
from matplotlib import cm
import matplotlib.pyplot as plt
import math
import numpy as np
import sys
from player import Player
from population import Population

def one_run(population,iterations):
    mediasp=[]
    mediasq=[]
    mediap=0
    mediaq=0
    imtag = 0
	#Make sure population size is a square number
    side_size = math.floor(math.sqrt(population.size))
    fitnessMatrix = np.zeros((side_size, side_size))
    for t in range(iterations):
        p1=population.randomPlayer()
        tag = p1.tag
        i = math.floor(tag / side_size)
        j = tag % side_size
        p2=population.randomNeighbor(p1)
        f1=population.getFitness(p1)
        f2=population.getFitness(p2)
        if f2>f1:
            population.imitate(p1,p2)
        fitnessMatrix[i, j] = population.getFitness(p1)
        m=population.media()   
        mediasp+=[m[0]]
        mediasq+=[m[1]]
        if t>=(iterations-100):
            mediap+=m[0]
            mediaq+=m[1]
        if t % 400 == 0:
            print("Saving frame at", t)
            pylab.imshow(fitnessMatrix, interpolation='nearest', cmap=cm.Blues, vmin=0, vmax=4.1)
            pylab.axis('off')
            pylab.savefig('Frames/frame' + str(imtag), bbox_inches='tight')
            imtag += 1
    
    #make_graph(population)
    plt.scatter(list(range(len(mediasp))),mediasp)
    plt.show()
	#TODO: Save graphs in Graphs folder
    return (mediap/(100),mediaq/(100))

def main():
    n=20
    e=0.001
    iterations=2*80000
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
