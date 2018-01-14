import Book;
import PythonBook;

book = Book.Book(price=15, name="name", author="zuozhe");
book.price = 20;

book.setName("haah");
book.show();

####继承

pythonBook = PythonBook.PythonBook(type="ebook");  # 继承了Book的构造器
pythonBook.setName("zhzz")
pythonBook.showInfo()
pythonBook.doSomething()


# 多重继承
class A:
    name = "A";
    __num = 1;

    def show(self):
        print(self.name);
        print(self.__num);

    def setNum(self, num):
        self.__num = num;


class B:
    nameb = "B";
    __numb = 2;

    def show(self):
        print(self.nameb);
        print(self.__numb);

    def setName(self, name):
        self.nameb = name;


class C(A, B):
    def showAll(self):
        print(self.name);
        print(self.nameb);


C = C();
C.showAll()
C.show()  # 由于A B都有show()方法,因此该出调用结果是根据继承顺序有关class C(B,A). 所以这一打印的是 A 1
C.setNum(3)
C.setName("zhu");
C.showAll()
