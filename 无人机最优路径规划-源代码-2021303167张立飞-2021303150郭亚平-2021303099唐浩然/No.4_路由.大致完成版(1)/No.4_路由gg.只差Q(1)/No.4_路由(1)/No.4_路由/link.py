# import collections


class Link:
    def __init__(self, ports: tuple, length=10 ** 4, datasize=100, delay=5, tag=0):
        self.length: int = length  # 链路长度
        self.ports: tuple = ports  # 链路两端连接的节点序号
        self.delay: float = delay  # 起飞时延
        self.occupation: int = 0  # 链路上飞机的占用量
        self.max_datasize: int = datasize  # 链路能承载的最大飞机数
        self.tag: int = tag  # 设置链路通信状况的标志位，这里默认为0

    def occupy_link(self, data_size):
        # 进入链路的飞机
        if self.occupation + data_size <= self.max_datasize:
            self.occupation += data_size
            return True
        else:
            return False

    def release_link(self, data_size):
        # 释放链路，传入数据大小
        if self.occupation >= data_size:
            self.occupation -= data_size
            return True
        else:
            return False

    def update_link_info(self, new_info):
        # 更新链路信息，例如延迟、最大飞机数量等
        if self.occupation >= self.max_datasize:
            self.tag = 1
        else:
            self.tag = 0

    def get_link_info(self):
        # 查询链路信息，例如延迟，链路上的飞机占用量等
        print(getattr(Link, "delay"))
        print(getattr(Link,"occupation"))
        return

    def update_link_info(self, start, end, new_info):
        # 更新连接信息，例如延迟或标志位
        self.G[start][end]['weight'] = new_info

    def get_length(self):
        #查询链路长度
        print(getattr(Link, "length"))
