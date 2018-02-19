import networkx as nx

G = nx.Graph()
G.add_edges_from([(1,2),(1,3)])
G.add_node(1)
G.add_edge(1,2)
G.add_node("lover")
G.add_nodes_from("lover")
G.add_edge(3,'e')

G.number_of_edges()
G.number_of_nodes()
