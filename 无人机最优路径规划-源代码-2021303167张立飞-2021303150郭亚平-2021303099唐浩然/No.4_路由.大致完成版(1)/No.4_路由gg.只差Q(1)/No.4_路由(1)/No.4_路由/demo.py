'''
demo.py中存放了城市网络的拓补图相关信息的测试（非项目文件），后续建立拓补图的代码部分放net.py中
'''

import matplotlib.pyplot as plt
import networkx as nx
from itertools import islice

# import numpy

from net import Net
from router import Router
from link import Link
from plane import Plane
import tkinter as tk

# 创建城市地图
city_map = Net()

'''解释一下：datasize这里指的是节点上可以容纳的最大飞机数目'''

router1 = Router(number=1, name="壶口瀑布", requirement=20, datasize=30)
router2 = Router(number=2, name="安定门",  requirement=15, datasize=25)
router3 = Router(number=3, name="大雁塔",  requirement=20, datasize=25)
router4 = Router(number=4, name="黄帝陵",  requirement=25, datasize=28)
router5 = Router(number=5, name="回民街",  requirement=35, datasize=35)
router6 = Router(number=6, name="小雁塔",  requirement=75, datasize=30)
router7 = Router(number=7, name="小寨",  requirement=35, datasize=32)
router8 = Router(number=8, name="大唐芙蓉园", requirement=38, datasize=27)
router9 = Router(number=9, name="大唐不夜城",  requirement=55, datasize=25)
router10 = Router(number=10, name="秦始皇兵马俑",  requirement=35, datasize=35)
router11 = Router(number=11, name="长恨歌",  requirement=55, datasize=27)
router12 = Router(number=12, name="华清宫", requirement=25, datasize=33)
router13 = Router(number=13, name="钟楼", requirement=35, datasize=31)
router14 = Router(number=14, name="永宁门", requirement=43, datasize=26)
router15 = Router(number=15, name="碑林博物馆", requirement=33, datasize=27)
router16 = Router(number=16, name="长乐门", requirement=61, datasize=30)
router17 = Router(number=17, name="陕西历史博物馆", requirement=30, datasize=35)
router18 = Router(number=18, name="西安城墙", requirement=35, datasize=28)
router19 = Router(number=19, name="永兴坊", requirement=45, datasize=27)
router20 = Router(number=20, name="曲江书城", requirement=35, datasize=30)

# 添加地标节点到城市地图
city_map.add_landmark(router1)
city_map.add_landmark(router2)
city_map.add_landmark(router3)
city_map.add_landmark(router4)
city_map.add_landmark(router5)
city_map.add_landmark(router6)
city_map.add_landmark(router7)
city_map.add_landmark(router8)
city_map.add_landmark(router9)
city_map.add_landmark(router10)
city_map.add_landmark(router11)
city_map.add_landmark(router12)
city_map.add_landmark(router13)
city_map.add_landmark(router14)
city_map.add_landmark(router15)
city_map.add_landmark(router16)
city_map.add_landmark(router17)
city_map.add_landmark(router18)
city_map.add_landmark(router19)
city_map.add_landmark(router20)

# 创建连接示例
'''这里的datasize指的是链路上可容纳的最大飞机数，delay指的是飞机正常飞过的额外延迟'''
# link1 = Link(ports=(1, 10), length=100, datasize=20, delay=8)
link2 = Link(ports=(10, 18), length=80, datasize=30, delay=6)
link3 = Link(ports=(1, 4), length=25, datasize=15, delay=6)
link4 = Link(ports=(4, 12), length=80, datasize=40, delay=6)
link5 = Link(ports=(2, 4), length=2, datasize=45, delay=7)
link6 = Link(ports=(5, 7), length=2, datasize=15, delay=7)
link7 = Link(ports=(2, 5), length=30, datasize=20, delay=5)
link8 = Link(ports=(4, 7), length=50, datasize=35, delay=7)
link9 = Link(ports=(7, 10), length=50, datasize=40, delay=6)
link10 = Link(ports=(7, 13), length=70, datasize=25, delay=7)
link11 = Link(ports=(7, 11), length=40, datasize=20, delay=5)
link12 = Link(ports=(4, 3), length=2, datasize=30, delay=7)
link13 = Link(ports=(3, 6), length=25, datasize=40, delay=8)
link14 = Link(ports=(6, 7), length=1, datasize=35, delay=6)
link15 = Link(ports=(10, 11), length=70, datasize=45, delay=7)
link16 = Link(ports=(11, 12), length=80, datasize=15, delay=7)
link17 = Link(ports=(12, 13), length=65, datasize=30, delay=5)
link18 = Link(ports=(13, 14), length=75, datasize=15, delay=7)
# link19 = Link(ports=(6, 14), length=55, datasize=20, delay=8)
link20 = Link(ports=(8, 14), length=45, datasize=25, delay=7)
link21 = Link(ports=(8, 9), length=50, datasize=30, delay=6)
link22 = Link(ports=(9, 17), length=70, datasize=25, delay=7)
link23 = Link(ports=(9, 20), length=80, datasize=35, delay=6)
link24 = Link(ports=(13, 17), length=100, datasize=30, delay=7)
link25 = Link(ports=(17, 20), length=90, datasize=40, delay=5)
link26 = Link(ports=(16, 20), length=85, datasize=15, delay=8)
link27 = Link(ports=(19, 20), length=95, datasize=30, delay=7)
link28 = Link(ports=(13, 16), length=70, datasize=25, delay=6)
link29 = Link(ports=(16, 19), length=65, datasize=20, delay=7)
link30 = Link(ports=(13, 15), length=60, datasize=15, delay=6)
link31 = Link(ports=(15, 19), length=45, datasize=35, delay=7)
link32 = Link(ports=(10, 15), length=80, datasize=20, delay=5)
link33 = Link(ports=(15, 18), length=70, datasize=25, delay=7)
link34 = Link(ports=(1, 2), length=15, datasize=30, delay=8)
link35 = Link(ports=(18, 19), length=75, datasize=15, delay=7)

# 添加连接到城市地图
# city_map.add_link(link1)
city_map.add_link(link2)
city_map.add_link(link3)
city_map.add_link(link4)
city_map.add_link(link5)
city_map.add_link(link6)
city_map.add_link(link7)
city_map.add_link(link8)
city_map.add_link(link9)
city_map.add_link(link10)
city_map.add_link(link11)
city_map.add_link(link12)
city_map.add_link(link13)
city_map.add_link(link14)
city_map.add_link(link15)
city_map.add_link(link16)
city_map.add_link(link17)
city_map.add_link(link18)
# city_map.add_link(link19)
city_map.add_link(link20)
city_map.add_link(link21)
city_map.add_link(link22)
city_map.add_link(link23)
city_map.add_link(link24)
city_map.add_link(link25)
city_map.add_link(link26)
city_map.add_link(link27)
city_map.add_link(link28)
city_map.add_link(link29)
city_map.add_link(link30)
city_map.add_link(link31)
city_map.add_link(link32)
city_map.add_link(link33)
city_map.add_link(link34)
city_map.add_link(link35)

# print(router1.get_requirement())
# print(router3.get_name())
# print(link1.get_link_info())
# print(city_map.find_short_path('1', '10'))
# 创建飞机实例

start_node = '2'  # 起始节点标号
target_node = '20'  # 终止节点标号
plane_size = 600  # 飞机的大小
initial_delay = 10  # 初始延迟
target_numsize = 2  # 目标路径的数量

plane_instance1 = Plane(start=start_node, target=target_node, numsize=target_numsize, size=plane_size,
                        delay=initial_delay)

# 访问飞机实例属性
print("飞机的起始节点标号:", plane_instance1._start)
print("飞机的终止节点标号:", plane_instance1._target)
# plane_instance1.simulate_flight(city_map)
# print(plane_instance1.logs)
result = plane_instance1.simulate_flight(city_map, target_numsize)
print(result)

# 显示城市拓扑图
city_map.show_graph()
