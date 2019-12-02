import networkx as nx
import numpy as np
import pandas as pd
import itertools
import matplotlib.pyplot as plt
from collections import Counter
import powerlaw

#TODO: Make graph creation optional

data=pd.read_csv("BAAD.csv",sep=',',index_col=0)
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
#           Support Functions
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


def getOrganizationsThatAttackedInACountry():
    country_org_dic = {}
    for country in data:
        country_org_dic[country] = data.index[data[country] == 1].tolist()
    
    return country_org_dic


def get_number_of_attacks_per_organization():
    organizations = {}
    for row in list(data.index.values):
        organizations[row] = 0
        for attack in data.loc[row]:
            if attack == 1:
                organizations[row] += 1
    return organizations


# shows number of locations that were attacked only once
def locationsAttackedNTimes(lst_numbers):
    countries = get_number_of_attacks_per_country()
    lst = []
    
    for country in countries:
        if countries[country] in lst_numbers:
            lst += [country]

    return lst

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




# -----------------------------------------------
#
#			Additional Calculations
#
# -----------------------------------------------


# -------------------------------------
#			Average Degree
# -------------------------------------

#Nodes, Edges and Average Degree
def getAvgDegree():
    numNodes = len(graph.nodes())
    numEdges = len(graph.edges())
    avgDegree = (2 * numEdges) / numNodes
    print("Average degree: {}".format(avgDegree))


# -------------------------------------
#		  Degree Distribution
# -------------------------------------

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


# -------------------------------------
#		  Average Path Length
# -------------------------------------    

def getAveragePathLength():
    sum1 = 0
    sum0 = 0
    for scc in nx.connected_component_subgraphs(graph):
        if nx.average_shortest_path_length(scc) == 1:
            sum1 += 1
        else:
            sum0 += 1
    
    print("Number of SCC with average path length equal to 0: {}\nNumber of SCC with average path length equal to 1: {}".format(sum0, sum1))



# -------------------------------------
#		  Clustering Coefficient
# -------------------------------------

def clusteringCoefficient():
    print("Clustering Coefficient = {}".format(nx.average_clustering(graph)))


def clusteringCoefficientForNode():
    sum1 = 0
    sum0 = 0
    dic = nx.clustering(graph)

    for org in dic:
        if dic[org] == 1:
            sum1 += 1
        else:
            sum0 += 1 
    
    print("Nodes with clustering coefficient of 0: {}\nNodes with clustering coefficient of 1: {}".format(sum0, sum1))


def checkOrgsWithZeroClusteringCoef():
    dic = nx.clustering(graph)

    # organizations with 0 clustering coefficient
    lst = [] 

    for org in dic:
        if dic[org] == 0:
            lst += [org]
    
    locations_lst = locationsAttackedNTimes([1,2])
    country_orgs_dic = getOrganizationsThatAttackedInACountry()
    
    # organizations that attacked in countries that were attacked only once or twice
    lst_2 = []

    for location in locations_lst:
        lst_2 += country_orgs_dic[location]
    lst.sort()
    lst_2.sort()

    if lst == lst_2:
        print("Nodes with clustering coefficient equal to 0 are the organizations that attacked in countries that were attacked in total either once or twice")


# -------------------------------------
#    Strongly Connected Components
# -------------------------------------

def stronglyConnectedComponents():
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
    plt.title('Strongly Connected Components Distribution')
    plt.ylabel('Relative Frequencies')
    plt.xlabel('Size of Components')
    plt.show()


def getNumberOfStronglyConnectedComponents():
    a=list(nx.strongly_connected_components(graph.to_directed()))
    print("Number of Strongly Connected Components:", len(a))



# -----------------------------------------------
#
#			    Print Results
#
# -----------------------------------------------


print("Number of Nodes:", len(graph.nodes()))
print("Number of Edges:", len(graph.edges()))
getAvgDegree()
getAveragePathLength()
clusteringCoefficient()
clusteringCoefficientForNode()
getNumberOfStronglyConnectedComponents()
print()
plot = input("Choose the plot you want to see:\n\t1 - Degree Distribution\n\t2 - Strongly Connected Components\n Choice: ")
if plot == "1":
    degreeDistribution()
else:
    stronglyConnectedComponents()

