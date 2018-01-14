"""
第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
"""
import os;
import sys;


class Test:
    def count_code(self, file):
        total_line = 0;
        empty_line = 0;
        comment_line = 0;
        print(file)
        if file.endswith('.idea'):
            return 0,0,0;
        fileObject = open(file,"r");
        for line in fileObject:
            # split
            wordList = line.split();
            if wordList == []:
                empty_line += 1;
            elif wordList[0] == '#':
                comment_line += 1;
            else:
                total_line += 1;
        fileObject.close();
        return total_line, empty_line, comment_line

if __name__ =='__main__':
    test = Test();
    t_lines = 0
    e_lines = 0
    c_lines = 0
    dir = "/Users/zhuyang/projects/python_learning/practice";
    for fileName in os.listdir(dir):
        filePath = os.path.join(dir,fileName);
        if os.path.isdir(filePath):
            continue;
        t,e,c = test.count_code(filePath);
        t_lines+=t;
        e_lines+=e;
        c_lines+=c;
    print("total line is %d , comment line %d , empty line %d" % (t_lines,c_lines,e_lines))