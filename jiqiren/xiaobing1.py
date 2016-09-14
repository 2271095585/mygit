#-*-encoding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import urllib2
from urllib import urlencode
from urllib import quote
import pprint
import time


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
             'Content-Length': str(str(data)),
             'Content-Type': 'application/x-www-form-urlencoded',
             'Host': 'api.weibo.com',
             'Referer': 'http://api.weibo.com/chat/',
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'}
    cookie ={'ALF': '1503980108',
             'Apache': '4375420690052.9136.1472444070362',
             'JSESSIONID': '59FD88653E3AB2D1787C39DC9282912D',
             'SINAGLOBAL': '4375420690052.9136.1472444070362',
             'SSOLoginState': '1472444108',
             'SUB': '_2A2563IMaDeTxGeNM6FQS8ibEwzSIHXVZq_PSrDV8PUNbmtBeLUX3kW9OZ5VCqRNdenazpSDMGFjLsIpYcA..',
             'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WFzEqE9SMqhjcMLzezzACqI5JpX5KzhUgL.Fo-Ee0q0eonR1hn2dJLoI7fjIPS79PikIg4_dN9L',
             'SUHB': '0gHSd2GVmA-USw',
             'ULV': '1472444070372:1:1:1:4375420690052.9136.1472444070362:',
             '_s_tentry': '-',
             'login_sid_t': 'd55acb17441748dd74670ad72853128a',
             'wvr': '6'}
    r = requests.post(url,headers=header,cookies=cookie,data=data)
    print r
    print r.content
    print '=================================================================='

def ew_read():
    f = open('ask.txt').readlines()
    a = 0
    for i in f[5500:6000]:
        if i == '\n':
            pass
        else:
            word = i.replace('\n','')
            print word
            xiaobing(word)
            time.sleep(3)
            print a
            a += 1

ew_read()
























