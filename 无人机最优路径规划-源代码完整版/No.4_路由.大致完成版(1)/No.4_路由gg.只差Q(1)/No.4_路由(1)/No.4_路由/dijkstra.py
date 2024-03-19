'''Dijkstra算法求最短路（gpt写的），结果没测试不过应该没问题，可以和另一种选路方法一起用'''
''''''

import heapq


def dijkstra(start, end):
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
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {}  # 用于跟踪每个节点的前一个节点
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node  # 更新前一个节点
                heapq.heappush(priority_queue, (distance, neighbor))

    # 构建最短路径
    path = []
    while end is not None:
        path.insert(0, end)
        end = previous_nodes.get(end)

    return path


'''
graph = {
    1: {2: 1, 3: 7},
    2: {1: 1, 3: 9, 4: 5},
    3: {1: 2, 2: 2, 4: 1},
    4: {2: 5, 3: 5}
}

start_node = 1
end_node = 4

shortest_path = dijkstra(graph, start_node, end_node)

print(f"从节点 {start_node} 到节点 {end_node} 的最短路径是: {shortest_path}")
'''

