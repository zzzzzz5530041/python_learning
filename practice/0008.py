'''一个HTML文件，找出里面的正文。'''

import urllib.request;
import re;
def getBody(url):
    htmlContent = urllib.request.urlopen(url).read();
    r = re.compile('<p>(?:<.[^>]*>)?(.*?)(?:<.[^>]*>)?</p>');
    html=htmlContent.decode('utf-8')
    result = r.findall(html)
    return result
if __name__=='__main__':
    body = getBody("http://blog.csdn.net/lxh199603/article/details/53192883")
    resultFile = open("result",mode="w");
    for line in body:
        resultFile.write(line)
    resultFile.close()
