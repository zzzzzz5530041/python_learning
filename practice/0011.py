"""
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge
"""
import os;
import sys;


def filtWords(word):
    fileObj = open("/Users/zhuyang/projects/python_learning/practice/filtered_words", "r");
    filtered_words = []
    for line in fileObj:
        filtered_words.append(line.strip('\n'))
    fileObj.close()

    # Check if the input words include the filtered words
    filtered = False
    for filtered_word in filtered_words:
        if filtered_word in word:
            filtered = True
            break

    if filtered is True:
        print('Freedom')
    else:
        print('Human Rights')

if __name__ == '__main__':
    while True:
        input_words = input('Input some words:')
        filtWords(input_words)

