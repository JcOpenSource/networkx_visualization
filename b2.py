import matplotlib.pyplot as plt 
import networkx as nx
import pandas as pd
import numpy as np
from scipy import optimize

# 0.csv数据导入
f = open('topology.csv')
data = pd.read_csv(f)

# 1.建图
G = nx.Graph()
edge_list = []
for indexs in data.index:
    source = data.loc[indexs].values[0]
    target = data.loc[indexs].values[1]
    edge_list.append((source, target))
G.add_edges_from(edge_list)

# 2.节点度
Degree = list(G.degree())
degree = []
for value in G.degree():
    degree.append(value[1])

# 3.多分别于x轴是节点度数，y轴是度数的次数
# 获得节点度数的set
degree_set = set(degree)

ans = {}
for value in degree_set:
    count = 0
    for d in degree:
        if d == value:
            count += 1
    ans[value] = count

x_degree = []
y_count = []
for (key, value) in ans.items():
    x_degree.append(key)
    y_count.append(value)


# 4.拟合函数
# 定义了一个目标函数，幂律分布为P（k）=cx 的(-r)次方，利用编程求出c r的值
def func(x, a, b):
    return a * x**b


a, b = optimize.curve_fit(func, x_degree, y_count)
x = range(2000)
y2 = a[0]*x**(a[1])
print("a[0]是", a[0], "a[1]是", a[1])

# 绘制双对数坐标
# plt.style.use("ggplot")
plt.scatter(np.log(x_degree), np.log(y_count), alpha=0.8, c="green", marker='x')
plt.scatter(np.log(x), np.log(y2), alpha=0.5, c="b")
plt.show()
