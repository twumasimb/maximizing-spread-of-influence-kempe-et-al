import networkx as nx
import matplotlib.pyplot as plt
def create_graph(no_of_nodes):

    """
        This function creates a fully connnected multi-edge directed graph
    """
    graph = nx.MultiDiGraph()
    node_list = range(1, (no_of_nodes+1))
    graph.add_nodes_from(node_list)

    return create_edges(graph)

def create_edges(graph):
    """
        This function will create a fully connected bidirectional graph
    """

    edges = []

    for i in range(1, len(graph.nodes)+1):
        for j in range(1, len(graph.nodes)+1):
            if (i != j):
                x = (i, j)
                edges.append(x)
    print("The Edges are : ", edges)
    graph.add_edges_from(edges)

    print("This is the new graph:", graph.nodes())
    print("These are the detail sof the edges: ", graph.edges())
    
    return graph

graph = create_graph(20)
print(graph.nodes())

nx.draw(graph)
plt.show()