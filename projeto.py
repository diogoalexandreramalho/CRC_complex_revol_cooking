import networkx as nx
import numpy as np
import pandas as pd
import itertools
import matplotlib.pyplot as plt
from collections import Counter
import powerlaw

#TODO: Make graph creation optional

data=pd.read_csv("../BAAD.csv",sep=',',index_col=0)
graph = nx.Graph()
dic={}
c=0

# -----------------------------------------------
#
#				Graph Creation
#
# -----------------------------------------------

for org in data.index.values:
    graph.add_node(org)
    dic[c]=org
    c+=1
for country in data:
    col=data[country]
    lst=[]
    for i in range(len(col)):
        if col[i]==1:
            lst+=[i]
    if len(lst)>1:
        for edge in itertools.combinations(lst, 2):
            n1=dic[edge[0]]
            n2=dic[edge[1]]
            graph.add_edge(n1,n2,attr=country)
nx.write_gexf(graph, "graph.gexf")



# -----------------------------------------------
#
#           Functions
#
# -----------------------------------------------


def get_total_number_of_attacks():
    sum = 0
    for country in data:
        for value in data[country]:
            sum += value
    return sum
    

def get_number_of_attacks_per_country():
    countries = {}
    
    for country in data:
        countries[country] = 0
        for num in data[country]:
            countries[country] += num
    
    return countries


def get_number_of_attacks_per_organization():
    organizations = {}
    for row in list(data.index.values):
        organizations[row] = 0
        for attack in data.loc[row]:
            if attack == 1:
                organizations[row] += 1
    return organizations



# -----------------------------------------------
#
#			Additional Calculations
#
# -----------------------------------------------

#Nodes, Edges and Average Degree
def getAvgDegree():
    numNodes = len(graph.nodes())
    numEdges = len(graph.edges())
    avgDegree = (2 * numEdges) / numNodes
    return avgDegree

def degreeDistribution():
    dgDistribution = []
    numNodes = len(graph.nodes())

    for node in graph.nodes():
    	dgDistribution.append(graph.degree(node))

    #averages array is created for plotting
    degrees = Counter(dgDistribution)
    averages = []

    for el in degrees:
        averages.append(degrees[el] / numNodes)

    plt.title('Degree Distribution')
    plt.ylabel('Relative Frequencies')
    plt.xlabel('Degree')
    plt.scatter(list(degrees), averages)
    plt.show()


def getNumberOfStronglyConnectedComponents():
    a=list(nx.strongly_connected_components(graph.to_directed()))
    return len(a)
    

def getAveragePathLength():
    for scc in nx.connected_component_subgraphs(graph):
        print(nx.average_shortest_path_length(scc))


# proves that all organizations attack once
def allOrganizationsAttackOnce():
    sum = 0
    organizations = get_number_of_attacks_per_organization()
    for org in organizations:
        if organizations[org] == 1:
            sum += organizations[org]
        else:
            print(org)
    return sum 


def clusteringCoefficient():
    print(nx.average_clustering(graph))


clusteringCoefficient()


"""
a=list(nx.strongly_connected_components(graph.to_directed()))

sizeComponents=[]
for i in list(a):
    sizeComponents+=[len(i)]


numComponents=len(sizeComponents)



fit = powerlaw.Fit(np.array(sizeComponents)+1,xmin=1,xmax=72,discrete=True)
fit.power_law.plot_pdf( color= 'b',linestyle='--',label='fit ccdf')

print('alpha= ',fit.power_law.alpha,'  sigma= ',fit.power_law.sigma)


sizeComponents= Counter(sizeComponents)

averages=[] 
for el in sizeComponents:
    averages.append(sizeComponents[el] / numComponents)





plt.scatter(list(sizeComponents),averages)
plt.show()"""




