#-*-encoding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import urllib2
from urllib import urlencode
from urllib import quote
import time


def answer_get(word):
    url = 'http://www.tuling123.com/api/product_exper/chat.jhtml'
    data = {
        'key':'efebeec191e447828f650896daa00327',
        'info':word,
        'userid':'hhly419'
    }
    r = requests.post(url,data=data)
    print r
    print r.content
    answer =  r.content.split("<Content><![CDATA[")[1].split("]]")[0]
    print answer
    return answer
    
def ew_read():
    f = open('ask.txt').readlines()
    a = 0
    for i in f:
        word = i.replace('\n','')
        print word
        try:
            if word == '':
                ff = open("answer_tuling.txt",'a')
                ff.write('\n')
                ff.close()
            else:
                answ = answer_get(word)
                time.sleep(0.5)
                result = word + "  ==answer==  " + answ + '\n'
                ff = open("answer_tuling.txt",'a')
                ff.write(result)
                ff.close()
                print a
                a += 1
        except:
            ef = open("err.txt",'a')
            ef.write(i)
            ef.close()


ew_read()


# answer_get("下午好")