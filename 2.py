import networkx as nx
import community
import matplotlib.pyplot as plt

# 0.构图 空手道数据集
G = nx.karate_club_graph()

# 1.louvain 社区发现
communities = community.best_partition(G)

# 2.根据社区编号着色
color = list(communities.values())

# 3.绘图
nx.draw(G,
        with_labels=True,
        node_color=color,
        pos=nx.spring_layout(G, k=0.2, iterations=50), alpha=0.76)

plt.show()
