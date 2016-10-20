#-*-encoding:utf-8-*-
import requests
import time


def answer_get(word):
    url = 'http://www.tuling123.com/api/product_exper/chat.jhtml'
    data = {
        'key':'efebeec191e447828f650896daa00327',
        'info':word,
        'userid':'hy419'
    }
    r = requests.post(url,data=data)
    answer =  r.content.split("<Content><![CDATA[")[1].split("]]")[0]
    print word,' === ',answer
    return answer
    
def ew_read():
    f = open('ask.txt').readlines()[16000:20000]
    a = 0
    for i in f:
        word = i.replace('\n','').strip()
        try:
            if word == 'HHLY':
                ff = open("answer_tuling.txt",'a')
                ff.write('HHLY\n')
                ff.close()
            else:
                answ = answer_get(word.decode('gbk').encode('utf8'))
                time.sleep(0.5)
                result = word.decode('gbk').encode('utf8') + "  ==answer==  " + answ + '\n'
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