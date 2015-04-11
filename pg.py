import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
G.add_node(1,a='a')
G.add_node(2,b='b')
G.add_node(3,c='c')
G.add_edges_from([(1,2),(2,3),(1,3)])
nx.draw(G)
plt.show()
