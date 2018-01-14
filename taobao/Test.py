import os
import ssl
import time
import urllib.request

from bs4 import BeautifulSoup
from selenium import webdriver

ssl._create_default_https_context = ssl._create_unverified_context
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
feedbackPath='';
def getProductList(url):  # 传入搜索URL
    res = urllib.request.urlopen(url).read();


def getProductImg(url):
    htmlContent = urllib.request.urlopen(url).read();
    soup = BeautifulSoup(htmlContent, "html.parser");
    title = soup.title.string
    path = "/Users/zhuyang/projects/python_learning/" + title;
    global feedbackPath;

    feedbackPath = path + "/feedback"
    if os.path.exists(path):
        return;
    os.makedirs(path, exist_ok=True);  # 创建文件夹
    os.makedirs(feedbackPath, exist_ok=True);  # 创建买家秀文件夹

    # descDiv = soup.findAll("div",{"id":"J_DivItemDesc"});
    scriptContent = scritContent = soup.findAll("script");
    reg1 = r"descUrl.*?location.protocol==='http:' \? '//(.*?)'.?:"
    desurlre = re.compile(reg1)
    descUrl = '';
    # 获得产品描述页面
    for sc in scriptContent:
        desurls = re.findall(desurlre, sc.text);
        if len(desurls):
            descUrl = desurls[0];
            print(descUrl)
            parseDesc("http://" + descUrl, path)
        else:
            continue;


def parseDesc(url, path):
    htmlContent = urllib.request.urlopen(url).read();
    soup = BeautifulSoup(htmlContent, "html.parser");
    imageTags = soup.findAll("img");
    imageList = [];
    for imgTag in imageTags:
        img = imgTag.get("src");
        imageList.append(img);
    downLoadImg(imageList, path)


def downLoadImg(images, path):
    i = 1;
    for img in images:
        print(img);
        print(i)
        i += 1;
        try:
            urllib.request.urlretrieve(img, path + "/" + str(i) + str(img)[-5:]);
        except:
            continue;



def search(keyword):
    urls = [];
    keywords = urllib.request.quote(keyword)
    url = "https://s.taobao.com/search?q=" + keywords
    # url="https://s.taobao.com/search?q="+keywords+"&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&s="+str(i*44)
    htmlContent = url_open(url);
    driver = webdriver.PhantomJS(executable_path='/etc/phantomjs-2.1.1-macosx/bin/phantomjs');
    # driver = webdriver.Firefox()
    driver.get("http://taobao.com")
    driver.get(url)
    time.sleep(1)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, 'mainsrp-itemlist')))
    data = driver.find_element_by_id("mainsrp-itemlist");
    '''
    <div class="pic">
        <a href="" />>
    </div>
    '''
    tags = data.find_elements_by_class_name("pic");
    for tag in tags:
        links = tag.find_elements_by_tag_name("a");
        for link in links:
            urls.append(link.get_attribute("href"));

    # 遍历url
    for url in urls:
        print(url)
        try:
            id = url[url.find("=") + 1:url.find("&")];
            if str.isdigit(id):
                getProductImg(url)
                getFeedbackImg(id);

        except:
            continue;


# 打开网页，获取网页内容
def url_open(url):
    headers = ("user-agent",
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
    return data


def getFeedbackImg(id):
    print("feedbackPath"+feedbackPath)
    imageUrls=[];
    url = "https://rate.taobao.com/feedRateList.htm?auctionNumId=" + id + "&currentPageNum=1&pageSize=20&rateType=3";
    content = url_open(url);
    content = content.strip().strip('()');#数据格式:({..}),去掉两边的括号,处理json
    json_dic = json.loads(content);
    comments = json_dic['comments'];
    for c in comments:
        appendList = c['appendList'];
        for a in appendList:
            photos = a['photos'];
            for p in photos:
                imageUrl = p['url']
                imageUrls.append(imageUrl)
        append = c['append'];
        for a in appendList:
            photos = a['photos'];
            for p in photos:
                imageUrl = p['url']
                imageUrls.append(imageUrl)
        photosNodes = c['photos'];
        for p in photosNodes:
            imageUrl = p['url']
            imageUrls.append(imageUrl)
    i=0;
    for imgUrl in imageUrls:
        print(imgUrl);
        i += 1;
        try:
            urllib.request.urlretrieve("http:"+imgUrl, feedbackPath + "/" + str(i) + str(imgUrl)[-5:]);
        except:
            continue;


#getFeedbackImg("543890771574")
print(search('欧恰恰'));

# getProductImg("https://item.taobao.com/item.htm?spm=a230r.1.14.60.ba33c737iXaSr&id=543890771574&ns=1&abbucket=6#detail")
# getFeedbackImg("https://rate.taobao.com/feedRateList.htm?auctionNumId=543890771574&currentPageNum=1&pageSize=20&rateType=3")
# getProductList( "https://item.taobao.com/item.htm?id=39595400262")
# https://rate.taobao.com/feedRateList.htm?auctionNumId=543890771574&currentPageNum=1&pageSize=20&rateType=3 评论
