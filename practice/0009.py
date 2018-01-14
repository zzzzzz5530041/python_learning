'''

一个HTML文件，找出里面的链接。
'''
import re;
import urllib.request


def findLink(url):
    htmlContent = urllib.request.urlopen(url).read();
    htmlContent=htmlContent.decode("utf-8")
    print(htmlContent)
    r = re.compile("href='(.*?)'");
    result = r.findall(htmlContent)
    return result


if __name__ == '__main__':
    print(findLink('http://blog.csdn.net/lxh199603/article/details/53192883'))
