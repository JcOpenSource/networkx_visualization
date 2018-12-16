import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

edge_list = pd.read_csv('stack_network_links.csv')

G = nx.from_pandas_edgelist(edge_list)

plt.figure(figsize=(20, 20))

nx.draw(G, with_labels=True,
        edge_color='grey',
        node_color='blue',
        node_size=10,
        pos=nx.spring_layout(G, k=0.2, iterations=50))
# iterations 迭代优化，没有将距离相近的节点拉近。
# k是每个节点之间的距离【0，1】越大距离越远。

plt.show()
