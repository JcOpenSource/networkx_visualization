import networkx as nx
import matplotlib.pyplot as plot

G = nx.karate_club_graph()
nx.draw(G, with_labels=True)

plot.show() 