from utils import greedy
import random
import pickle

# Working on the fairness data
graph = pickle.load(open('networks/graph_spa_500_0.pickle','rb')) 

# finding the coverage for each number of nodes
nodes_covered = []
number_of_networks = 10000
for k in range(1, 31):
    cover = greedy(graph, number_of_networks,  k)
    total_cover = sum(cover[1])
    nodes_covered.append(total_cover)
    print(f'Iter {k}')
