import re
# r=re.search('1\w+','231422sadf',re.S|re.I)
# print(r.span())#返回在字符串的位置
# print(r.group())#调用对象的group方法获得字符串
# import json
# a={'a':'1111','b':'2222','c':'3333','d':'4444'}
# r=json.dumps(a)
# # print(type(r))
# print(r)


# line = "Cats are smarter than dogs";
#
# searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
# print(searchObj)



# print(re.match('www', 'www.runoob.com').group())  # 在起始位置匹配
# print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配
a=10
def f():
    global c
    c=16
    # print(c)
f()
# print(c)