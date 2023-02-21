from graph_fx import create_graph
from models import weighted_icm,icm

graph = create_graph(20)

weighted_icm_graph = weighted_icm(graph=graph)

icm_graph = icm(graph, 0.1)

