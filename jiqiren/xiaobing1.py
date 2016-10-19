#-*-encoding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import urllib2
from urllib import urlencode
from urllib import quote
import pprint
import time
import random


def space_delete():
    f = open('EW.txt').readlines()
    a = 0
    for i in f:
        if i == '\n':
            pass
        else:
            ff = open("ask.txt",'a')
            ff.write(i)
            ff.close()

# space_delete()




def xiaobing(word):
    url = 'http://api.weibo.com/chat/2/direct_messages/new.json?source=209678993'
    data = {
        'text':word,
        'uid':'5175429989'
    }
    # print len(str(data))
    header = {'Accept': 'application/json, text/plain, */*',
             'Accept-Encoding': 'gzip, deflate',
             'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
             'Connection': 'keep-alive',
             'Content-Length': str(len(data)),
             'Content-Type': 'application/x-www-form-urlencoded',
             'Host': 'api.weibo.com',
             'Referer': 'http://api.weibo.com/chat/',
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'}
    cookie ={'ALF': '1505699386',
                 'Apache': '4744624779336.184.1474163371801',
                 'SINAGLOBAL': '4375420690052.9136.1472444070362',
                 'SSOLoginState': str(int(time.time())),
                 'SUB': '_2A2565NT9DeTxGeNJ6VIS9CzOwjuIHXVZkEE1rDV8PUNbmtBeLWvAkW9jxYbH84mdXEvJoSfOFCt8lXxURA..',
                 'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9W5EblZ6ZZJ6-aqQ.QnpYIsc5JpX5KzhUgL.Fo-Neo50ShzE1KM2dJLoIE8uINyuINnLxKnLBKqL1h2LxK-LB.eL1h5LxK-LB.qL1het',
                 'SUHB': '0rrLyFBdRUDiaT',
                 'ULV': '1474163371806:3:2:1:4744624779336.184.1474163371801:1473835808783',
                 'UOR': ',,graph.qq.com',
                 '_s_tentry': '-',
                 'crossidccode': 'CODE-gz-1BLreK-24PhH5-R6mfQUPtz3YTY125b9fa4',
                 'login_sid_t': '571f4b18a18df3d2e08228e29aada979',
                 'wvr': '6'}
    r = requests.post(url,headers=header,cookies=cookie,data=data)
    print r
    print r.content
    print '=================================================================='

def ew_read():
    f = open('ask.txt').readlines()
    a = 0
    for i in f[12500:]:
        if i == '\n':
            pass
        else:
            word = i.replace('\n','')
            print word
            xiaobing(word)
            t_r = random.randint(3, 4)
            time.sleep(int(t_r))
            print a
            a += 1

ew_read()
























