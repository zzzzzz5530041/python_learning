# 标准输入
# s = input("input name:");
# print("your input is %s " % (s) )

##文件io
'''
标识符:

r 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。

rb 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。

r+ 打开一个文件用于读写。文件指针将会放在文件的开头。

rb+ 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。

w 打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。

wb 以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。

w+ 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。

wb+ 以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。

a 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。

ab 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。

a+ 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。

ab+ 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

作者：相关函数
链接：https://www.jianshu.com/p/f6b7db275f44
來源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

'''
file = open("test", mode='r');  # 打开文件并返回文件对象
for line in file.readlines():
    print(line.strip())
    # 将内容写入test2
    file2 = open('test2', mode='a');  ## mode = a 表示内容追加,
    file2.writelines(line)

# StringIO & ByteIO
'''
很多时候读数据不一定是从文件中读, 还有可能从内存中读. 要读取StringIO,需要先从io中导入StringIO.

写入数据到StringIO中,需要先创建一个StringIO.然后像文件一样写入即可.调用getvalue()方法获得写入的str
'''
from io import StringIO;

f = StringIO();
s = "hellow word";
# 写入到缓存
f.writelines(s);
# 从缓存读取
print(f.getvalue())

# 操作文件和目录
import os;

print(os.path.abspath("."))  ##当前文件绝对路径
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
newDirPath = os.path.join(os.path.abspath("."), "newdir");
print(newDirPath)
if os.path.exists(newDirPath):  # 如果目录存在, 删除
    os.rmdir(newDirPath)
##新建目录
os.mkdir(newDirPath)

##序列化
'''
我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling.序列化之后，
就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上.反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
'''

# 序列化一个dict
import pickle

d = dict(name="zhuyang", age="20", sex="male");
f = open("serial.data", "wb");
pickle.dump(d, f);  # pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
f.close();

# 反序列化
f = open("serial.data", 'rb');
d = pickle.load(f);
print(d)
f.close();

# json
import json;

d = dict(name="zhuyang", age="20", sex="male");
str = json.dumps(d);  # 返回string
print(str)
# 反序列化是调用loads()方法
d = json.loads(str)
print(d);


class Student(object):
    def __init__(self, name, age, sex):
        self.name = name;
        self.age = age;
        self.sex = sex;


stu = Student("zhuyang", 20, "male");


# 将stu转成dict
def obj2dic(stu):
    return dict(name=stu.name, age=stu.age, sex=stu.sex);


# 序列化
jsonStr = json.dumps(obj2dic(stu));
print(jsonStr);


# 反序列化
def dict2Stu(dict):
    return Student(dict["name"], dict["age"], dict["sex"]);


o = json.loads(jsonStr, object_hook=dict2Stu)
print(o)  # <__main__.Student object at 0x102ad4128>
