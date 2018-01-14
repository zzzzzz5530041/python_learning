class MyStack:
    def __init__(self, size=10):
        self.stack = [];  # 定义堆栈列表
        self.size = size;  # 堆栈长度
        self.top = -1;  # 栈顶位置

    def setSize(self, size):
        self.size = size;

    def push(self, element):
        if self.isFull():
            raise StackException("stack fullll");
        else:
            self.stack.append(element);
            self.top = self.top + 1;

    def pop(self):
        if self.isEmpty():
            raise StackException("stack empty");
        else:
            element = self.stack[-1]  ##取得列表最后一条数据
            self.top = self.top - 1;
            del self.stack[-1];  # 删除最后一条数据
            return element;

    def topElement(self):
        return self.stack[-1];  # 获取栈顶数据

    def top(self):
        return self.top;  # 获取栈顶位置

    def empty(self):
        self.stack = [];
        self.top = -1;

    def isEmpty(self):
        if self.top == -1:
            return True;
        else:
            return False;

    def isFull(self):
        if self.top == self.size - 1:
            return True;
        else:
            return False;


class StackException(Exception):  # 自定义异常
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data


if __name__ == '__main__':
    stack = MyStack();
    for i in range(20):
        stack.push( i);
    print(stack.pop())
