#-*-encoding:utf-8-*-
import pprint

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

word = """JSESSIONID=57F1C757C9DEE02F5DA2C88478CC1BA5; BIGipServerotn=972030474.50210.0000; _jc_save_fromStation=%u6DF1%u5733%u5317%2CIOQ; _jc_save_toStation=%u5E7F%u5DDE%u5357%2CIZQ; _jc_save_fromDate=2016-12-11; _jc_save_wfdc_flag=dc"""
# header_get(word)
cookie_get(word)