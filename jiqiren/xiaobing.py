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
    header = {
        'Host': 'api.weibo.com',
        'Connection':'keep-alive',
        'Content-Length':str(str(data)),
        'Accept': 'application/json, text/plain, */*',
        'Origin': 'http://api.weibo.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'http://api.weibo.com/chat/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
    cookie ={
        "SINAGLOBAL":"8326686124783.01.1470023832340",
        "_s_tentry":"www.99.com.cn",
        "Apache":"2526642889676.096.1471332290214",
        "ULV":"1471332290379:5:5:1:2526642889676.096.1471332290214:1470811838474",
        "SSOLoginState":"1471428809",
        "wvr":"6",
        "SCF":"ArUx4TLS-7bmiMtoSe_BLrdRVAHEzKouwwbvdUrtGWzcY3o4KJ_KDWSIoPeJ4lq90iC3O1nkX9Snad_qUHJC6IA.",
        "SUB":"_2A256-dUsDeTxGeNJ6VIS9CzOwjuIHXVZj0HkrDV8PUNbmtAKLRPzkW8WmDSAWTmo0UAi7HDquRTvNl3VlA..",
        "SUBP":"0033WrSXqPxfM725Ws9jqgMF55529P9D9W5EblZ6ZZJ6-aqQ.QnpYIsc5JpX5K2hUgL.Fo-Neo50ShzE1KM2dJLoIE8uINyuINnLxKnLBKqL1h2LxK-LB.eL1h5LxK-LB.qL1het",
        "SUHB":"05iK-EO_A3me2V",
        "ALF":"1503364867",
        "UOR":"www.baidu.com,weibo.com,www.baidu.com",
    }

    r = requests.post(url,headers=header,cookies=cookie,data=data)
    print r
    print r.content
    print '=================================================================='

def ew_read():
    f = open('ask.txt').readlines()
    a = 0
    for i in f:
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
























#微博小冰信息抓取
# t = str(int(time.time()))
# print t
# url = 'http://0.44.web1.im.weibo.com/im/connect?jsonp=jQuery21408148183246462171_1471485159686' \
#       '&message=%5B%7B%22channel%22%3A%22%2Fmeta%2Fconnect%22%2C%22connectionType%22%3A%22callback-polling%22%2C%22id%22%3A%2226%22%2C%22clientId%22%3A%22otn1eb7ry03n5u1c1p52qq096l26q%22%7D%5D' \
#       '&_=' + t
#
# header = {
# 'Host': '0.44.web1.im.weibo.com',
# 'Connection': 'keep-alive',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
# 'Accept':' */*',
# 'Referer': 'http://api.weibo.com/chat/',
# 'Accept-Encoding': 'gzip, deflate, sdch',
# 'Accept-Language': 'zh-CN,zh;q=0.8'
# }
# cookie = {
# "SINAGLOBAL":"8326686124783.01.1470023832340",
# "_s_tentry":"www.99.com.cn",
# "Apache":"2526642889676.096.1471332290214",
# "ULV":"1471332290379:5:5:1:2526642889676.096.1471332290214:1470811838474",
# "SSOLoginState":"1471428809",
# "wvr":"6",
# "SCF":"ArUx4TLS-7bmiMtoSe_BLrdRVAHEzKouwwbvdUrtGWzcB03QHI-5X32ZK9lIW_YwsPdYCXS6gnguKaiFXLNlAY0.",
# "SUB":"_2A256sElCDeTxGeNJ6VIS9CzOwjuIHXVZxD2KrDV8PUNbmtANLVDEkW-BVuz1CCEo8UvqsNTVtfNNCz0hFw..",
# "SUBP":"0033WrSXqPxfM725Ws9jqgMF55529P9D9W5EblZ6ZZJ6-aqQ.QnpYIsc5JpX5K.hUgL.Fo-Neo50ShzE1KM2dJLoIE8uINyuINnLxKnLBKqL1h2LxK-LB.eL1h5LxK-LB.qL1het",
# "SUHB":"0BLYEC57vMJsnD",
# "ALF":"1472033681",
# "BAYEUX_BROWSER":"69da-uqi9dfdkwb9xiryr74idkwq",
# "UOR":"www.baidu.com,weibo.com,www.baidu.com",
# "JSESSIONID":"nt1dy3e5yk8kah11z372zwd5"
# }
#
# r = requests.get(url,headers=header,cookies=cookie)
# print r
# print r.headers
# print r.cookies
# print r.content
