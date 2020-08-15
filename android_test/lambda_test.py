# def add(x,y):
#     return x+y
# #匿名函数
# r=lambda x,y:x+y
# ss=r(1,2)
# print(ss)
#三元表达式
# x=3
# y=2
# r=x if x>y else y
# print(r)

# def square(x):
#     return x**2
#
# list1=[1,2,3,4,5]
# list2=[2,3,4,5,6]
# result=map(lambda x:x**2,list1)
# ss=map(lambda x,y:x+y,list1,list2)
# bb=map(square,list1)
# print(list(result))
# print(list(ss))
# print(type(bb))
# for i in bb:
#     print(i)
# print(next(bb))
# print(next(bb))
# print(next(bb))
# ab=[1,2]
# cd=[3,4]
# ef=ab+cd
# print(ef)
from functools import reduce
# ll=[1,2,3,4,5]
# sport=[(0,0),(1,3),(2,-1)]
# ff=reduce(lambda x,y:x+y,sport)
# print(ff)




list1=[1,2,1,4,6,1]
list2=['a','B','c','D']
f=filter(lambda x:x.istitle(),list2)
for i in f:
    print(i)
# print(list(f))
# print(f)
# print(type(f))