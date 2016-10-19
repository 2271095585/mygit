#-*-encoding:utf-8-*-
import requests
import sys
sys.path.append("..")
import pprint
from tool_my import commen
import time
import random
import pymongo
import pprint
import requests
import math
from bs4 import BeautifulSoup


# commen.space_delete('answer_tuling_new.txt','answer_tuling.txt')
user_dict = {"lifeng200545":"lifeng419",
              "lifeng419":"hhly419",
              "inmove":"allen12345",
              "tulingweibo":"tulinghhly419",
              "tulingweixin":"tulingw419"}

def tuling_key_get(user,password):
    header1= {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
     'Accept-Encoding': 'gzip, deflate, sdch',
     'Accept-Language': 'zh-CN,zh;q=0.8',
     'Cache-Control': 'max-age=0',
     'Connection': 'keep-alive',
     'Host': 'www.tuling123.com',
     'Upgrade-Insecure-Requests': '1',
     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    header = {'Accept': 'application/json, text/javascript, */*; q=0.01',
     'Accept-Encoding': 'gzip, deflate',
     'Accept-Language': 'zh-CN,zh;q=0.8',
     'Connection': 'keep-alive',
     'Content-Length': '35',
     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
     'Host': 'www.tuling123.com',
     'Origin': 'http://www.tuling123.com',
     'Referer': 'http://www.tuling123.com/login/index.jhtml',
     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
     'X-Requested-With': 'XMLHttpRequest'}
    header2 = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
     'Accept-Encoding': 'gzip, deflate, sdch',
     'Accept-Language': 'zh-CN,zh;q=0.8',
     'Connection': 'keep-alive',
     'Host': 'www.tuling123.com',
     'Referer': 'http://www.tuling123.com/login/index.jhtml',
     'Upgrade-Insecure-Requests': '1',
     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    url_login = 'http://www.tuling123.com/login/index.jhtml'
    url_index = 'http://www.tuling123.com/login/to_login.jhtml'
    url_key = 'http://www.tuling123.com/member/center/index.jhtml'
    r = requests.get(url_login,headers=header1)
    cookie = { "JSESSIONID":r.cookies["JSESSIONID"]}
    data = {"username":user,
            "password":password}
    rr = requests.post(url_index,headers=header,cookies=cookie,data=data)
    cookie = dict({'CNZZDATA1000214860':'293344727-1471510246-%7C1474509527'},**cookie)
    print cookie
    rrr = requests.get(url_key,headers=header2,cookies=cookie)
    print rrr
    soup = BeautifulSoup(rrr.content,"lxml")
    key = soup.select(".perMsg > p")[-1].select("span")[0].get_text()
    print key
    return key

for k,v in user_dict.items():
    key = tuling_key_get(k,v)
    print k,v,key


