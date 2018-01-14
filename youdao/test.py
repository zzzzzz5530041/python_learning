# encoding=utf-8
import os;
import sys;

root = "/Users/zhuyang/Documents/Youdao/SYNC";

fileCount = 0;


def iterateFolder(path):
    print("iterate path %s" % (path));
    if os.path.isdir(path):
        print("current path: %s is folder..continue to iterate" % (path));
        dirs = os.listdir(path);
        for dir in dirs:
            iterateFolder(os.path.join(root, path+dir))
    else:
        global fileCount;
        print("current path: %s is file.." % (path));
        fileCount = fileCount + 1;
    return fileCount


if __name__ == '__main__':
    print(iterateFolder(root))
