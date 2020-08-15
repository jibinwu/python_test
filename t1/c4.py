# a=[1,2,3]
# a.append(4)
# # a.pop(1)
# print(a)
# b=[4,5,6]
# c=a+b
# print(c)

# a={1,2,3}
# b={4,5,6}
# c=a+b
# print(c)
# a='/   http://www.baidu.com'
# print(a.strip('/').strip())

# a=1000
# b=1.0*1000
# c=10*100
# d=10*100
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))
# print(a is b)
# print(a==b)

# import time
# a=time.time()
# print(type(a))


# def add(x,y):
#     return x+y
# a=add(1,3)
# print(a)
#
# f=lambda x:x+1
# print(f(2))

# def w1(func):
#     def inner():
#         # 验证1
#         # 验证2
#         # 验证3
#         func()  #f1()
#     return inner    #把f1函数也塞进去了
#
# @w1
# def f1():
#     print('装饰器有点意思!')
# # f1()
# a=w1(f1)
# print(a())


from time import ctime, sleep

def timefun(func):
    def wrappedfunc(a,b):
        print("%s called at %s"%(func.__name__, ctime()))
        print(a,b)
        func(a,b)
    return wrappedfunc

@timefun
def foo(a,b):
    print(a+b)

foo(3,5)
# foo(2,4)


# #定义函数：完成包裹数据
# def makeBold(fn):
#     def wrapped():
#         return "<b>" + fn() + "</b>"
#     return wrapped
#
# #定义函数：完成包裹数据
# def makeItalic(fn):
#     def wrapped():
#         return "<i>" + fn() + "</i>"
#     return wrapped
#
# @makeBold
# def test1():
#     return "hello world-1"
#
# @makeItalic
# def test2():
#     return "hello world-2"
#
# @makeBold
# @makeItalic
# def test3():
#     return "hello world-3"
#
# if __name__ == '__main__':

    # print(test1())
# print(test2())
# print(test3())
import time
import requests


