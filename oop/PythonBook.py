import Book


class PythonBook(Book.Book):
    type = '';

    def __init__(self, type):
        self.type = type;

    def showInfo(self):
        self.show()
        print("type=" + self.type);
    def doSomething(self):
        print("do some in PythonBook")