import threading;


# 继承threading.Thread
class MyThread(threading.Thread):
    def __init__(self, num, threadName):
        ##调用弗雷的构造器
        threading.Thread.__init__(self, name=threadName);  # 设置线程名
        self.num = num;

    def run(self):
        print("i am ", self.num);


t1 = MyThread("thread 1 ", "t1");
t2 = MyThread("thread 2 ", "t2");
t3 = MyThread("thread 3 ", "t3");
t4 = MyThread("thread 4 ", "t4");
t1.start();
t2.start();
t3.start();
t4.start();
print(t1.getName())

'''
除了继承Thread外,还可以直接使用Thread创建县城
'''


def hello(name):
    print(name)


def go(x, y):
    for i in range(x, y):
        print(i);

def printNum():
    for i in range(20):
        print(i)
printNum()
t6 = threading.Thread(target=hello,kwargs=dict(name="hello"));
t6.start()
#t5 = threading.Thread(target=go, args=(10, 15), name="t5");
#t5.start();
#print(t5.isAlive)  # 打印线程状态
#print(t5.getName())

'''线程同步'''
