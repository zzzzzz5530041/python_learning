class Book:
    # constructor
    def __init__(this, name, price, author):
        this.__name = name;
        this.price = price;
        this.author = author;

    __name = "";
    price = 10;
    author = "zhuyang"

    def setName(this, name):
        this.__name = name;

    def show(this):
        print("author=" + this.author);
        print("name=" + this.__name);
        this.__printPrice();

    def __printPrice(this):  # 私有方法只能内部调用
        print("price=" + str(this.price))  # price是数字,因此需要转换成str

    def doSomething(self):
        print("do some in Book")
