#-*-encoding:utf-8-*-
import pprint

d = """_s_tentry=www.liaoxuefeng.com; Apache=9085287592609.355.1472270958542; SINAGLOBAL=9085287592609.355.1472270958542; ULV=1472270958550:1:1:1:9085287592609.355.1472270958542:; login_sid_t=15e4d582bfd69ad878fabcc27c87d220; SSOLoginState=1472278603; un=18669969035; wvr=6; BAYEUX_BROWSER=9a481p98l4kjuru15iscswyz7uh4; SUB=_2A256xvhzDeTxGeNJ6VIS9CzOwjuIHXVZsm67rDV8PUJbmtANLVDzkW-LMC8F97RV71lWXkVPG04N1RuYPg..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5EblZ6ZZJ6-aqQ.QnpYIsc5JpX5o2p5NHD95QfS0z7e0BEeo.NWs4DqcjyIc_RIc_Ri--Ri-2ciKnpi--fi-ihiKn7i--fi-isiKn0; SUHB=0ElqKfMderpgap; ALF=1503902546; UOR=www.liaoxuefeng.com,widget.weibo.com,www.findspace.name; JSESSIONID=1blpbo03c0emfdni5g9znk097"""
#header转化
def header_get(word):
    headers = {}
    header_list = word.strip().split("\n")
    for h in header_list:
        if 'HTTP/' in h:
            pass
        else:
            h_k,h_v = h.split(':',1)
            headers[h_k.strip()] = h_v.strip()
    pprint.pprint(headers)
    return headers

#cookie转化
def cookie_get(word):
    cookies = {}
    cookie_list = word.split(";")
    for c in cookie_list:
        c_k,c_v = c.split("=",1)
        cookies[c_k.strip()] = c_v.strip()
    pprint.pprint(cookies)
    return cookies

# cookie_get(d)

#去除文件空格
def space_delete(file_old,file_new):
    f = open(file_old).readlines()
    for i in f:
        if i == '\n':
            pass
        else:
            ff = open(file_new,'a')
            ff.write(i)
            ff.close()


