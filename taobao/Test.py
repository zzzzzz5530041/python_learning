import os
import ssl
import time
import urllib.request
import threadpool;
from bs4 import BeautifulSoup
from selenium import webdriver
import threading

ssl._create_default_https_context = ssl._create_unverified_context
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

feedbackPath = '';


def getProductList(url):  # 传入搜索URL
    res = urllib.request.urlopen(url).read();


def getProductImg(url):
    htmlContent = urllib.request.urlopen(url).read();
    soup = BeautifulSoup(htmlContent, "html.parser");
    title = soup.title.string
    path = NEW_IMAGE_ROOT_PATH + "/" + title;
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
            #不爬取商户图片
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


def getFeedbackImg(id):
    print("feedbackPath" + feedbackPath)
    imageUrls = [];
    url = "https://rate.taobao.com/feedRateList.htm?auctionNumId=" + id + "&currentPageNum=1&pageSize=20&rateType=3";
    content = url_open(url);
    content = content.strip().strip('()');  # 数据格式:({..}),去掉两边的括号,处理json
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
    i = 0;
    if imageUrls is None:
        print("no feedback...");
        os.rmdir(feedbackPath);
    for imgUrl in imageUrls:
        print(imgUrl);
        i += 1;
        try:
            print("-------------"+NEW_IMAGE_ROOT_PATH);
            if os.path.exists(os.path.join(NEW_IMAGE_ROOT_PATH,"feedback")) ==False:
                os.mkdir(os.path.join(NEW_IMAGE_ROOT_PATH,"feedback"))

            urllib.request.urlretrieve("http:" + imgUrl, NEW_IMAGE_ROOT_PATH + "/feedback/" + str(i) + str(imgUrl)[-5:]);

        except:
            continue;


def search(keyword, paginationIdentifier):
    urls = [];
    keywords = urllib.request.quote(keyword)
    url = "https://s.taobao.com/search?q=" + keywords + "&s=" + str(paginationIdentifier) + "&sort=sale-desc"
    print(url)
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
                # getProductImg(url);
                productImgThread = threading.Thread(target=getProductImg, kwargs=dict(url=url),
                                                    name="load product img thread");
                productImgThread.start();
                feedBackimgThread = threading.Thread(target=getFeedbackImg, kwargs=dict(id=id),
                                                     name="load feedback img thread");
                feedBackimgThread.start();

                #   getFeedbackImg(id);

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



# getFeedbackImg("543890771574")
keyword = "波西米亚雪纺";
IMAGE_ROOT_PATH = "/Users/zhuyang/Documents/zhuyang/tb/";
NEW_IMAGE_ROOT_PATH = os.path.join(IMAGE_ROOT_PATH, keyword);
if os.path.exists(NEW_IMAGE_ROOT_PATH) == False:
    os.mkdir(NEW_IMAGE_ROOT_PATH)
for i in range(5,20):
    searchThread = threading.Thread(target=search, kwargs=dict(keyword=keyword, paginationIdentifier=i * 44));
    searchThread.start()



# getProductImg("https://item.taobao.com/item.htm?spm=a230r.1.14.60.ba33c737iXaSr&id=543890771574&ns=1&abbucket=6#detail")
# getFeedbackImg("https://rate.taobao.com/feedRateList.htm?auctionNumId=543890771574&currentPageNum=1&pageSize=20&rateType=3")
# getProductList( "https://item.taobao.com/item.htm?id=39595400262")
# https://rate.taobao.com/feedRateList.htm?auctionNumId=543890771574&currentPageNum=1&pageSize=20&rateType=3 评论

#https://s.taobao.com/search?type=similar&app=i2i&rec_type=1&nid=543890771574 like