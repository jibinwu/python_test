import re
# from time import ctime,sleep
# def timefun(func):
#     def warppedfunc():
#         print('%s called at %s'%(func.__name__,ctime()))
#         func()
#     return warppedfunc
#
# @timefun
# def foo():
#     print("I am foo")
# foo()
# sleep(2)
# foo()



#闭包
# def line_conf(a, b):
#     def line(x):
#         return a*x + b
#     return line
#
# line1 = line_conf(1, 1)
# line2 = line_conf(4, 5)
# print(line1(5))
# print(line2(5))

# ret = re.match("[A-Z][a-z]*","Aabcdef")
# print(ret.group())

# ret = re.match("[a-zA-Z_][\w_]*","name1")
# print(ret.group())

# ret = re.match("[a-zA-Z_][\w_]*","_name")
# print(ret.group())


# ret = re.match("[a-zA-Z0-9_]{6}","12a3g45678")
# print(ret.group())
#
# ret = re.match("[a-zA-Z0-9_]{8,20}","1ad12f23s34455ff66")
# print(ret.group())

# ret = re.match("[1-9][0-9]","29")
# print(ret.group())

# ret=re.match('[\w]

# ret = re.match("[1-9]?\d|100","100")
# print(ret.group())

# ret = re.match("([^-]*)-(\d+)","010-12345678")



# ret = re.match(r"<(
# ret = re.split(r":| ","info:xiaoZhang 33 shandong")
# print(ret)

# s="This is a number 234-235-22-423"
# r=re.match("\D+(\d+-\d+-\d+-\d+)",s)
# print(r.group(1))


# ret=re.match(r"aa(\d+)ddd","aa2343ddd369ddd")
# print(ret.group())

# r='<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" \
# src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">'
# ret=re.search('https://.*?jpg',r)
# print(ret.group())
# ret=re.findall('https://.*jpg$',r)
# print(ret)


# import time
# print(time.time())
# print(time.ctime())
# print(time.localtime())


import time
def deco(func):
    def wrapper():
        starttime=time.time()
        func()
        endtime=time.time()
        msecs=(endtime-starttime)*1000
        print('time is %s ms'%msecs)
    return wrapper

@deco
def func():
    print('hello')
    time.sleep(1)
    print('world')

if __name__ == '__main__':
    f = func    #这里f被赋值为func,执行f()就是执行func()
    f()









