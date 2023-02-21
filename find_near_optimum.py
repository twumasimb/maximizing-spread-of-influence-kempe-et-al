import utils

# important variables
limit = 0.4
# creating my graph
G = utils.graph(10)

edges = [[1, 2], [2, 3], [3, 4], [1, 7], [1, 5], [2, 5], [3, 6], [4, 6], [
    4, 10], [5, 7], [5, 8], [6, 9], [6, 10], [7, 8], [8, 9], [9, 10]]

new_graph = utils.random_weighted_graph(G, edges, limit)

# utils.plot_graph(new_graph, "blue")

list_of_covered_nodes = utils.coverage(new_graph)

constraint = 3

chosen_nodes, nodes_covered = utils.greedy(list_of_covered_nodes, constraint)

print("The selected nodes are: ",chosen_nodes)
print("The selected sets are: ", nodes_covered)

sample_icm_grapths = utils.sample_live_icm(new_graph, 100)
print(sample_icm_grapths)