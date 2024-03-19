# import copy
# import time
from collections import deque


class Plane:
    def __init__(self, start, target, numsize, size=600, delay=0):
        self._start: str = start  # 起始节点标号
        self._target: str = target  # 终止节点标号
        self.delay: float = delay  # 计算数据包传送中经过的时间
        self.state: tuple = (0, start)  # 数据包的状态
        self.shortest_path: list = []  # 从起点到终点的最短路径
        self.log_delay: float = 0
        self.num: int = numsize  # 目标路径的数量
        self.total: int = 0  # 无人机花费的总时间
        self.logs: list = []  # 传递过程中记录的集合
        self.flying_drones: deque = deque()  # 飞行中的无人机队列

    # def plan_shortest_path(self, city_map, start, target):
    # 使用图算法计算最短路径
    # self.shortest_path = city_map.find_short_path(self._start, self._target)

    def simulate_flight(self, city_map, numsize):
        # 模拟飞行过程
        self.shortest_path = city_map.find_short_path(self._start, self._target, self.num)
        if numsize <= 0:
            return 0
        if numsize == 1:
            for i in range(len(self.shortest_path) - 1):
                current_node = self.shortest_path[i]
                next_node = self.shortest_path[i + 1]
                link = city_map.get_link(current_node, next_node)  # 获取连接信息
                flight_delay = link  # .delay  # 获取飞行延迟
                self.total += flight_delay
                self.state = (i + 1, next_node)
                self.logs.append(f"飞行从{current_node}到{next_node}, 消耗{flight_delay}秒")
            self.logs.append(f'总飞行时间{self.total}')
            return self.logs
        else:
            for j in range(1, numsize + 1):
                for i in range(len(self.shortest_path[j - 1]) - 1):
                    current_node = self.shortest_path[j - 1][i]
                    next_node = self.shortest_path[j - 1][i + 1]
                    link = city_map.get_link(current_node, next_node)  # 获取连接信息
                    flight_delay = link  # .delay  # 获取飞行延迟
                    self.total += flight_delay
                    self.state = (i + 1, next_node)
                    self.logs.append(f"飞行从{current_node}到{next_node}, 消耗{flight_delay}秒")
                self.logs.append(f'总飞行时间{self.total}')
            return self.logs

    def query_landmark_info(self, city_map, landmark_name):
        # 查询地标信息
        landmark = city_map.get_landmark_by_name(landmark_name)
        return landmark

    def update_landmark_info(self, city_map, landmark_name, new_info):
        # 更新地标信息
        landmark = city_map.get_landmark_by_name(landmark_name)
        landmark.update_info(new_info)

    def record_event(self, event):
        # 记录事件到日志
        self.logs.append(event)

    def all_simulate_flight(self):
        # 初始化飞行队列，将起始节点加入队列
        self.flying_drones.append((0, self._start))

        while self.flying_drones:
            time, node = self.flying_drones.popleft()
            self.logs.append((time, node))

            # 模拟无人机的飞行过程，根据需要的延迟时间进行等待
            if self.delay > 0:
                time += self.delay
                self.logs.append(('Delay', self.delay))

            # 到达目标节点，结束飞行
            if node == self._target:
                break

        # 模拟无人机的选择下一个节点的过程，假设无人机选择下一个节点为next_node
        next_node = self._target  # 这里假设下一个节点为目标节点
        self.flying_drones.append((time, next_node))

        return self.logs
