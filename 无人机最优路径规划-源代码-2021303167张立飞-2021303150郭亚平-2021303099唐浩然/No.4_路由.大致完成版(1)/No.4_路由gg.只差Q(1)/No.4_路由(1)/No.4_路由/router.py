import collections
from enum import Enum
from queue import Queue


class Router:
    def __init__(self, number: int, name: str, requirement: int, datasize: int):
        self.sign: int = number  # 节点序号
        self.name: str = name  # 节点名称
        self.requirement: int = requirement  # 节点需求
        self.datasize: int = datasize  # 节点容量
        self.is_accessible: bool = True  # 节点是否可到达，默认为可到达
        # self.neighbors = []

    # def update_requirement(self, supplies):
    # 更新物资需求信息
    # self.requirement.update(supplies)

    def get_requirement(self):
        # print(getattr(Router, "requirement"))
        return self.requirement

    def get_sign(self):
        # 获取节点序号
        # print(getattr(Router, "sign"))
        return self.sign

    def get_name(self):
        # 获取节点名字
        # print(getattr(Router, "name"))
        return self.name

    def get_datsize(self):
        # 获取节点名字
        # print(getattr(Router, "datasize"))
        return self.datasize


router1 = Router(number=1, name="长安十二时辰", requirement=20, datasize=30)
router2 = Router(number=2, name="安定门", requirement=15, datasize=25)
router3 = Router(number=3, name="大雁塔", requirement=20, datasize=25)
router4 = Router(number=4, name="黄帝陵", requirement=25, datasize=28)
router5 = Router(number=5, name="回民街", requirement=35, datasize=35)
router6 = Router(number=6, name="小雁塔", requirement=75, datasize=30)
router7 = Router(number=7, name="小寨", requirement=35, datasize=32)
router8 = Router(number=8, name="大唐芙蓉园", requirement=38, datasize=27)
router9 = Router(number=9, name="大唐不夜城", requirement=55, datasize=25)
router10 = Router(number=10, name="秦始皇兵马俑", requirement=35, datasize=35)
router11 = Router(number=11, name="长恨歌", requirement=55, datasize=27)
router12 = Router(number=12, name="华清宫", requirement=25, datasize=33)
router13 = Router(number=13, name="钟楼", requirement=35, datasize=31)
router14 = Router(number=14, name="永宁门", requirement=43, datasize=26)
router15 = Router(number=15, name="碑林博物馆", requirement=33, datasize=27)
router16 = Router(number=16, name="长乐门", requirement=61, datasize=30)
router17 = Router(number=17, name="陕西历史博物馆", requirement=30, datasize=35)
router18 = Router(number=18, name="西安城墙", requirement=35, datasize=28)
router19 = Router(number=19, name="永兴坊", requirement=45, datasize=27)
router20 = Router(number=20, name="曲江书城", requirement=35, datasize=30)

router_instances = {"长安十二时辰": router1, "安定门": router2, "大雁塔": router3, "黄帝陵": router4, "回民街": router5,
                    "小雁塔": router6, "小寨": router7, "大唐芙蓉园": router8, "大唐不夜城": router9,
                    "秦始皇兵马俑": router10,
                    "长恨歌": router11, "华清宫": router12, "钟楼": router13, "永宁门": router14,
                    "碑林博物馆": router15,
                    "长乐门": router16, "陕西历史博物馆": router17, "西安城墙": router18, "永兴坊": router19,
                    "曲江书城": router20}
