'''
任一个英文的纯文本文件，统计其中的单词出现的个数。
'''

import sys;


class Test:
    def word_count(self, path):
        file_object = open(path, mode="r");  # 打开文件
        wordNum = 0;
        for line in file_object:  # 一行一行读取文件
            line_list = line.split();
            wordNum += len(line_list);
        file_object.close();
        return wordNum;


if __name__ == '__main__':
    test = Test();
    if len(sys.argv) < 1:
        print("Need at least 1 parameter. Try to execute 'python 0004.py $image_path'");
    else:
        for infile in sys.argv[1:]:
            try:
                print("The total number of words is " + str(test.word_count(infile)));
            except IOError:
                print("errr");
                pass;
