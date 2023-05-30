from utils import greedy
import random
import pickle
import matplotlib.pyplot as plt

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

plt.plot(range(0, len(nodes_covered)), nodes_covered)
plt.ylabel("Active Set Size")
plt.show()

# Showing the diminishing return property
# For a 10 node seedset
k = 10
cover, gain = greedy(graph, 1,  k)
plt.plot(range(0, len(gain)), gain)
plt.ylabel("marginal gain")
plt.show()