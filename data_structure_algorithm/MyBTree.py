class MyBTree:
    def __init__(self, value):
        self.data = value;
        self.left = None;
        self.right = None;

    def insertLeft(self, value):
        self.left = MyBTree(value);
        return self.left;

    def insertRight(self, value):
        self.right = MyBTree(value);
        return self.right;

    def show(self):
        print(self.data);


if __name__ == '__main__':
    root = MyBTree('root');
    A = root.insertLeft('A');
    C = A.insertLeft('C');
    D = A.insertRight('D');
    F = D.insertLeft('F');
    G = D.insertRight('G');
    B = root.insertRight('B');
    E = B.insertRight('E');
    root.show();
    root.left.show();
    root.right.show();
