#-*-encoding:utf-8-*-

# f = open("answer_tuling_new.txt",'r').readlines()
# ask = open("ask.txt",'r').readlines()
#
# for j in range(0,len(f)):
#     if f[j] in ask:
#         d = f[j]
#         a_id = ask.index(d)
#         if f[j+1] != ask[a_id+1]:
#             result = 'ask:'+ d.strip() + " ==answer== " + f[j+1]
#             ff = open("answer_xiaobing4.txt",'a')
#             ff.write(result)
#             ff.close()
#             print result
f = open("answer_xiaobing4.txt",'r').readlines()
ff = list(set(f))
for d in ff:
    dd = open("answer_xiaobing44.txt","a")
    dd.write(d)
    dd.close()


