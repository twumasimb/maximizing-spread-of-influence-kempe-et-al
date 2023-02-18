import utils


# important variables
limit = 0.4
# creating my graph
G = utils.graph(10)

edges = [[1, 2], [2, 3], [3, 4], [1, 7], [1, 5], [2, 5], [3, 6], [4, 6], [
    4, 10], [5, 7], [5, 8], [6, 9], [6, 10], [7, 8], [8, 9], [9, 10]]

new_graph = utils.random_edge_weights(G, edges, limit)

utils.plot_graph(new_graph, "blue")

list_of_covered_nodes = utils.coverage(new_graph)