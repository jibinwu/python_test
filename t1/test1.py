import threading
# class A(object):
#     pass
# a=A()
# print(a)

#__new__与__init__的区别
# class A(object):
#     def __new__(cls, *args, **kwargs):
#         # return "abc"
#         return super(A, cls).__new__(cls)
# a=A()
# print(type(a))


# class A(object):
#     def __new__(cls, *args, **kwargs):
#         return "abc"
#     def __init__(self):
#         print("__init__方法被执行")
# a=A()
# print(a)

#浅拷贝与深拷贝的理解
# import  copy
# a1=["s1","s2"]
# # a=[1,2,a1]
# a=(1,2,a1)
# b=a
# c=copy.copy(a)
# d=copy.deepcopy(a)
# print("这是值打印")
# print(a1)
# print(a)
# print(b)
# print(c)
# print(d)
# print("这是地址打印")
# print(id(a1))
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))
# a1.append("s3")
# print("这是值打印")
# print(a1)
# print(a)
# print(b)
# print(c)
# print(d)
# print("这是地址打印")
# print(id(a1))
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))

#可变数据类型修改内容，内存地址不变
# a=["s1","s2"]
# print(id(a))
# a.append("s3")
# print(id(a))

#不可变数据类型修改直接开辟新的内存空间
# b=("w1","w2")
# print(id(b))
# b=("w1","w2","w3")
# print(id(b))

#位置参数、*args、默认参数、关键字可变参数（**kwargs）
# def fun1(a,*args,b=99,**kwargs):
#     print(type(a))
#     print(type(args))
#     print(type(b))
#     print(type(kwargs))
#     print(a)
#     print(args)
#     print(b)
#     print(kwargs)
# fun1(1,2,3,4,b=8,c=9,d=10)

# l=[x*x for x in range(1,11)]
# print(l)
# g=(x*x for x in range(1,11)if x%2==0)#如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# for x in g:
#     print(x)


class Person():
    __name="jbw"
    __age="18"
p=Person()
print(p._Person__name)
print()












