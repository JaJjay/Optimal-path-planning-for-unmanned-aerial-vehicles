import copy
import random
import time

import matplotlib.pyplot as plt
import networkx as nx
import numpy

from link import Link
from k_shortest_path import yen
from dijkstra import dijkstra


class Net:
    def __init__(self):
        self.G = nx.Graph()  # 生成图

    def add_landmark(self, router):
        # 添加地标节点到图中
        self.G.add_node(router.sign, name=router.name, requirement=router.requirement, accessible=router.is_accessible)

    def add_link(self, link):
        # 添加连接信息到图中
        self.G.add_edge(link.ports[0], link.ports[1], weight=link.delay)

    def show_graph(self):
        # 使用spring布局绘制图形
        pos = nx.spring_layout(self.G)
        nx.draw(self.G, pos, with_labels=True)

        # 添加显示权重的边标签
        labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels)

        # 显示绘图
        plt.show()

    def get_link(self, current_node, next_node):
        # 拓扑图
        graph = {
            '1': {'10': 100, '4': 50, '2': 60},
            '2': {'4': 70, '5': 60, '3': 50, '1': 60},
            '3': {'7': 100, '8': 55, '9': 60, '2': 50},
            '4': {'12': 80, '13': 40, '2': 70, '1': 50},
            '5': {'13': 80, '6': 70, '2': 60},
            '6': {'13': 45, '14': 55, '5': 70},
            '7': {'3': 100},
            '8': {'3': 55, '14': 45, '9': 50},
            '9': {'3': 60, '17': 70, '20': 80, '8': 50},
            '10': {'18': 80, '11': 70, '1': 100, '15': 80},
            '11': {'12': 80, '10': 70},
            '12': {'13': 65, '11': 80, '4': 80},
            '13': {'14': 75, '12': 65, '6': 45, '5': 80, '4': 40, '17': 100, '16': 70, '15': 60},
            '14': {'6': 55, '13': 75, '8': 45},
            '15': {'19': 45, '18': 70, '10': 80, '13': 60},
            '16': {'20': 85, '19': 65, '13': 70},
            '17': {'20': 90, '13': 100, '9': 70},
            '18': {'10': 80, '19': 75, '15': 70},
            '19': {'20': 95, '18': 75, '15': 45, '16': 65},
            '20': {'19': 95, '16': 85, '17': 90, '9': 80}
        }
        # 检查当前节点和下一个节点是否存在于城市地图中
        if current_node in graph and next_node in graph[current_node]:
            return graph[current_node][next_node]
        else:
            return None

    def find_short_path(self, start, end,n):
        # 找到最短路径
        # shortest_path = nx.shortest_path(self.G, source=start, target=end, weight='weight')
        if n <= 0:
            return 0
        if n == 1:
            shortest_path = dijkstra(start, end)
        else:
            shortest_path = yen(start, end, n)
        return shortest_path
