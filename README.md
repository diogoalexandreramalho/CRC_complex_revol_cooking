# Terrorists Organization Graph Analysis

## About the Project

The goal of this project was to create and analyse a graph by choosing a dataset and converting the existing information into a graph structure, following with the calculation of some of its properties. 

### Data

The chosen dataset represents a connection of terrorist organizations with locations where the organization acted. It is a binary matrix of dimensions $394 x 65$, located on the file `code/data/BAAD.csv`, where the rows are indexed by the organizations and the columns are indexed by the locations. If a given entry as a 1, it means that the organization in that row acted in the location in that column. If it is 0 it means the opposite.

### Analysis

The following properties were computed:
* Degree Distribution
* Strongly Connected Components
* Average Path Length
* Clustering Coefficient
* Centrality

## Contributors
The code was developed by André Ribeiro, Diogo Ramalho and Jorge Pacheco.
