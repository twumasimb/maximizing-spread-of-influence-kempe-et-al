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
    while(l <= len(node_list)):
        print("While loop has started running")
        for path in nx.shortest_path(graph, l):
            print("For loop has started running")
            paths.append(path)      # put all the paths from node l to the last node in an array
        # for i in range(0, len(paths)):
        #     list_of_nodes += paths[i] # concat all the paths
        print(f"Path for node {l} is: ", paths)
        set_of_nodes = set(paths) # convert the nodes in the paths to a set
        list_of_coverage.append(set_of_nodes)
        l += 1
        # Clear these before starting the iteration
        paths.clear()
        list_of_nodes.clear()  
        print(f"List of sets after iteration {l-1} is: ", list_of_coverage)
    return list_of_coverage

def random_weighted_graph(graph, edges, threshold):
    """
    This function assigns edges to the graph given a threshold of the weight of the edge.
    Any weight below the threshold will lead to the edge being deleted

    Tips: pass your graph here
          pass your edges here
          choose a threshold between 0 and 1
    """

    # graph = graph(no_of_nodes)  # Import the graph function
    
    # Creatting random edges
    weights = []
    for i in range(0, len(edges)):
        weights.append(random.random())

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

    print("Weighted Graph Created")

    return graph

def plot_graph(graph, color):
    """
    Pass the graph. The color must be passed as string
    """
    nx.draw(graph, with_labels=True, node_color=color) #draw the network graph 
    plt.figure()
    plt.show() #to show the graph by plotting it

def greedy(list_of_covered_nodes, k):
    
    nodes_covered = set()

    subsets = list_of_covered_nodes

    selected = []
    selected_nodes = []
    
    tempList = subsets

    k = k

    while(len(selected) < k):
        x = set()
        a = []
        for i in range(len(tempList)):
            x = tempList[i] - nodes_covered # save all new items that the set adds to the soln set
            a.append(x)
            print("subsets",a)
        index = a.index(max(a))
        nodes_covered = nodes_covered | tempList[index]
        print("Current Solution Set: ", nodes_covered)
        selected.append(tempList[index])
        tempList[index] = set() # set the selected set to a null set
        print('The selected sets are: ', selected)

        selected_nodes.append((index+1))   # adding one because indeces in python start from 0
    
    return selected_nodes, nodes_covered

# Code from The Group Influence Paper

def sample_live_icm(g, num_graphs):
    '''
    Returns num_graphs live edge graphs sampled from the ICM on g. Assumes that
    each edge has a propagation probability accessible via g[u][v]['p'].
    '''
    import networkx as nx
    live_edge_graphs = []
    for _ in range(num_graphs):
        h = nx.Graph()
        h.add_nodes_from(g.nodes())
        for u,v in g.edges():
            if random.random() < g[u][v]['p']:
                h.add_edge(u,v)
        live_edge_graphs.append(h)
    return live_edge_graphs
    