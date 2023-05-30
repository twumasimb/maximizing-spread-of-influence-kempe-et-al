#importing important libraries
import networkx as nx
import matplotlib.pyplot as plt
import random

# Adding weights to the ICM graph
def assign_weights(graph):
    for u,v in graph.edges():
        weight = 1/(graph.degree(v))
        graph[u][v]['weight'] = weight
    return graph

# Function to generate the graphs with random weights
def sample_w_icm(g, num_of_networks):
    gen_nets = []
    for n in range(num_of_networks):
        h = nx.Graph()
        h.add_nodes_from(g.nodes())
        for u,v in g.edges():
            if random.random() < g[u][v]['weight']:
                h.add_edge(u,v)
        gen_nets.append(h)
    return gen_nets

# Find the average coverage of a selected solution set over all the generated networks
def average_coverage(Set, list_of_graphs):
    list_of_nodes = list(Set)
    total_size = 0
    average_coverage = 0
    for graph in list_of_graphs:
        set_of_nodes_covered = set()
        if (len(list_of_nodes) == 0):
            average_coverage = 0
        else:
            for item in list_of_nodes:
                coverage_in_a_single_graph = nx.node_connected_component(graph, item)
                set_of_nodes_covered = set_of_nodes_covered.union(coverage_in_a_single_graph)
        size_of_coverage_in_the_graph = len(set_of_nodes_covered)
        total_size += size_of_coverage_in_the_graph
    average_coverage = total_size/len(list_of_graphs)
    
    return average_coverage

def get_nodes(graph):
    y = []
    for i in range(len(graph.nodes)):
        y.append(i)
    return y

def greedy(graph, num_of_networks, k):
    graph = assign_weights(graph)
    sampled_graph = sample_w_icm(graph, num_of_networks)
    S = set()
    list_of_nodes = get_nodes(sampled_graph[0])
    gain = []
    while(len(S)) < k:
        list_of_marginal_gains = []
        for item in list_of_nodes:
            A = set()
            A.add(item)
            A = A | S
            marginal_gain = average_coverage(A, sampled_graph) - average_coverage(S, sampled_graph)
            list_of_marginal_gains.append(marginal_gain)
        index = list_of_marginal_gains.index(max(list_of_marginal_gains))
        gain.append(max(list_of_marginal_gains))
        S.add(list_of_nodes[index])
        list_of_nodes.pop(index)
    return S, gain
