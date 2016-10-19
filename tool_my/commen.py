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

word = """POST /lemma/default/ShowLemmaDefault,$FinalBorder.$NewSearchBar.sf.sd HTTP/1.1
Host: baike.sogou.com
Connection: keep-alive
Content-Length: 140
Cache-Control: max-age=0
Origin: http://baike.sogou.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Referer: http://baike.sogou.com/v173080.htm?fromTitle=%E5%BE%B7%E5%B7%9E
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8
Cookie: CXID=783E41C7CED8195EAF5A82756182E599; SUV=00BE651278ED5B9A579F0FBA6AF21327; pgv_pvi=4826541056; sct=7; IPLOC=CN4403; GOTO=Af99044; SMYUV=1474884605365675; ad=Xyllllllll2gXZdqlllllVKE53olllllWnCbukllll9llllljOxlw@@@@@@@@@@@; SUID=000000001527860A579EC294000BCE7A; ssuid=9226894656; SNUID=5BD848C275734A6AA8C4052E76CD652F; sw_uuid=5152454277; ld=hlllllllll2gXZMclllllVkV7MllllllWnCbukllll9lllll9klll5@@@@@@@@@@; JSESSIONID=81620D6637D290EE5F3DEE2EA43C570F; token=9B014E77FBB8EA4878606E4D47681803423EAFB9; _ga=GA1.2.1608638842.1476781995; ww_searchWord=
"""
header_get(word)