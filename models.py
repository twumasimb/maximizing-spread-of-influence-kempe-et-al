def weighted_icm(graph):
    """
        This weighted Independent Cascade model uses the degree of the node 
        to set the influence probability
    """
    for u,v in graph.edges():
        weight_v = 1/(graph.degree(v))
        graph[u][v]['weight'] = weight_v
        weight_u = 1/(graph.degree(u))
        graph[v][u]['weight'] = weight_u

    return graph

def icm(graph, probability):
    """
        The Independent Cascade Model has the probability that a node 
        will be a activated assigned to each edge.
    """
    for u,v in graph.edges():
        graph[u][v]['weight'] = probability
    
    return graph

# Include the Linear Threshold Model in the near future.