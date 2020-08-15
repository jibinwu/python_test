# from datetime import datetime
# curtime=datetime.now()
# t=curtime.timestamp()
# # print(curtime)
# # print(t.timestamp())
# print(datetime.fromtimestamp(t))
# a,

# s='hello'
# b=s.replace('l','s')
# print(b)

# def aa():
#     pass
# print(type(aa))

# a=[1,2,3]
# print(len(a))


# def add(a,b):
#     return a+b,a-b
# m,n=add(1,10)
# print(m,n)
# a=[1,2,3]
# b=[4,5,6]
# a.extend(b)

# print(a)

# sum=lambda x,y:x+y
# a=sum(1,2)
# print(a)
# print(sum(1,2))


# a=[1,2,3,1,4,5,1,1]
# b=a.count('1')
# print(b)
# tel={1:'a',2:'b',3:'c'}
# print(list(tel.keys()))
# a=list(range(4))
# print(a)
# a=dict([(1,'a'),(2,'b'),(3,'c')])
# a[4]='d'
# print(a)
# print(a[3])

# def add(a,b):
#     print('这是加法功能')
# print(add(1,2))

#列表推导式
a=[i+2 for i in range(10) if i%2==0]
print(a)
#注意没有元组推导式，只是生成了一个生成器,可以用next()函数来打印出生成器的具体值
b=(i+1 for i in range(5))
# print(type(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
for i in b:
    print(i)

#集合推导式
c={i*2 for i in [1,1,3]}
print(c)
# 字典推导式
sq={'a':1,'b':2,'c':3}
d={v:k for k,v in sq.items()}
print(d)


