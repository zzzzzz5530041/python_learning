class MyQueue:
    def __init__(self, size=10):
        self.queue = [];
        self.size = size;
        self.end = -1;

    def setSize(self, size):
        self.size = size;

    def add(self, element):  # 添加一个元素
        self.queue.append(element);
        self.end = self.end + 1;

    def poll(self):  # 出队
        element = self.queue[0];
        self.queue = self.queue[1:]  # 第一个元素后的所有数据
        self.end = self.end - 1;
        return element;
