# importing the necessary libraries
import networkx as nx
import random
import matplotlib.pyplot as plt

def graph(no_of_nodes):
    """
    This function create a graph whose vertices are numbers from 1
    to the number of nodes specified by the user
    """
    G = nx.Graph()
    node_list = range(1, no_of_nodes+1)
    G.add_nodes_from(node_list)

    return G

def coverage(graph):
    """
    This function returns a list with all the paths of each of the nodes in order
    """
    l = 1
    paths = []
    list_of_coverage = []
    list_of_nodes=[]
    node_list = list(graph.nodes)
    while(l <= len(node_list)+1):
        for path in nx.all_simple_paths(graph, source=l, target=len((node_list)+1)):
            paths.append(path)      # put all the paths from node l to the last node in an array
        for i in range(0, len(paths)):
            list_of_nodes += paths[i] # concat all the paths
        set_of_nodes = set(list_of_nodes) # convert the nodes in the paths to a set
        list_of_coverage.append(set_of_nodes)
        l += 1
        # Clear these before starting the iteration
        paths.clear()
        list_of_nodes.clear()  
    return list_of_coverage

def random_edge_weights(graph, edges, threshold):
    """
    This function assigns edges to the graph given a threshold of the weight of the edge.
    Any weight below the threshold will lead to the edge being deleted

    Tips: pass your graph here
          pass your edges here
          choose a threshold between 0 and 1
    """
    # Creatting random edges
    weights = []
    for i in range(0, len(edges)):
        weights.append(random.randint(0,10)*0.1)

    weighted_edges = []
    weighted_edges = edges
    for i in range(0, len(edges)):
        weighted_edges[i].append(weights[i])

    # Get edges that have weights greater that 0.6
    new_edges = []
    for i in range(0, len(weighted_edges)):
        if(weighted_edges[i][2] > threshold):
            new_edges.append(weighted_edges[i])

    graph.add_weighted_edges_from(new_edges)  #add the weighted edges to the graph
    weighted_edges.clear() # clear the lsit

    return graph

def plot_graph(graph, color):
    """
    Pass the graph. The color must be passed as string
    """
    nx.draw(graph, with_labels=True, node_color=color) #draw the network graph 
    plt.figure()
    plt.show() #to show the graph by plotting it