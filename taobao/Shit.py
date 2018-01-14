import urllib.request
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def getCommodityComments(url):
    if url[url.find('id=')+14] != '&':
        id = url[url.find('id=')+3:url.find('id=')+15]
    else:
        id = url[url.find('id=')+3:url.find('id=')+14]
    url = 'https://rate.taobao.com/feedRateList.htm?auctionNumId='+id+'&currentPageNum=1'
    res = urllib.request.urlopen(url).read()
    jc = json.loads(res.strip('()'))
    max = jc['total']
    users = []
    comments = []
    count = 0
    page = 1
    print('该商品共有评论'+str(max)+'条,具体如下: loading...')
    while count<max:
        res = urllib.request.urlopen(url[:-1]+str(page)).read()
        page = page + 1
        jc = json.loads(res.strip('()'))
        jc = jc['comments']
        for j in jc:
            users.append(j['user']['nick'])
            comments.append( j['content'])
            print(count+1,'>>',users[count],'\n        ',comments[count])
            count = count + 1

getCommodityComments('https://item.taobao.com/item.htm?id=39595400262&')
