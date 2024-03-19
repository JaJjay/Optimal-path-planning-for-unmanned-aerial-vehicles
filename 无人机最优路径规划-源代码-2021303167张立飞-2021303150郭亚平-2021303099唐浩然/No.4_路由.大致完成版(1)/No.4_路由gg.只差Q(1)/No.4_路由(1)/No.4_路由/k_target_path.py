import heapq
import copy
from mimaxue import get_link


def k_yen(start, end, middle):
    graph = {
        '1': {'10': 100, '4': 50, '2': 6},
        '2': {'4': 70, '5': 60, '3': 5, '1': 6},
        '3': {'7': 1, '8': 55, '9': 60, '2': 5},
        '4': {'12': 80, '13': 40, '2': 70, '1': 50},
        '5': {'13': 80, '6': 70, '2': 60},
        '6': {'13': 45, '14': 55, '5': 70},
        '7': {'3': 1},
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
    k = 7
    shortest_paths = []
    k_paths = []
    filtered_paths = []
    cnt = 0
    time = 0
    for i in range(1, k + 1):
        distances = {node: float("inf") for node in graph}
        distances[start] = 0
        previous = {node: None for node in graph}
        queue = []
        heapq.heappush(queue, (0, start))
        while queue:
            distance, node = heapq.heappop(queue)
            if node == end:
                path = []
                current = end
                while current is not None:
                    path.append(current)
                    current = previous[current]
                path = list(reversed(path))
                shortest_paths.append(path)
                break
            for neighbor, cost in graph[node].items():
                new_distance = distance + cost
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = node
                    heapq.heappush(queue, (new_distance, neighbor))

        if i < k:
            # 创建原始图的副本以进行修改
            modified_graph = copy.deepcopy(graph)
            for path in shortest_paths:
                for j in range(len(path) - 1):
                    u, v = path[j], path[j + 1]
                    if v in modified_graph[u]:
                        modified_graph[u][v] = float("inf")

            graph = modified_graph

    # 从k条路径中筛选出经过中间结点的路径
    for path in shortest_paths:
        if middle in path:
            filtered_paths.append(path)
            cnt = cnt + 1
    # print(f"Final Paths:")
    # for i, path in enumerate(filtered_paths):
        # print(f"Path {i + 1}: {' -> '.join(path)}")

    # 统计等待时间
    time = 0
    total = []
    for j in range(1, cnt + 1):
        time = 0
        for i in range(len(filtered_paths[j - 1]) - 1):
            current_node = filtered_paths[j - 1][i]
            next_node = filtered_paths[j - 1][i + 1]
            link = get_link(current_node, next_node)
            m = len(filtered_paths[j - 1]) - i
            flight_delay = link * m  # 获取飞行延迟
            # print(flight_delay)
            time += flight_delay
        total.append(str(filtered_paths[j - 1]) + str(time))
    return total
    # print(f"Path {j + 1}总等待时间为{total}")

'''
# 起始节点、目标节点和路径数
start_node = '9'
end_node = '15'
middle_node = '16'
# 使用yen函数找到k条最短路径
result = k_yen(start_node, end_node, middle_node)
print(result)
'''