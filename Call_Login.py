# def add(name,age):#返回一个字典
#     # p={'名字':name,'年龄':age}
#     # p=[name,age]
#     # p=(name,age)
#     # return  p
#     return name,age
# result=add('季彬武',27)
# print(result)

# 返回字符串
# def add1(x,y):
#     return '什么鬼东西'
# a=add1(1,2)
# print(a)

# def damage(x,y):
#     a=x*3
#     b=y+5
#     return a,b
# result=damage(5,4)
# c,d=result
# print(c,d)
# print(type(result))


# def stu_info(name,sex,age=10,school='光明'):
#     print('我的名字叫：'+name)
#     print('我今年'+str(age)+'岁')
#     print('我是'+sex+'生')
#     print('我来自'+school+'小学')
#     return  '这是'+name+'同学的信息'
#
#
# result=stu_info('季彬武','男',age=16,school='希望')
# print(result)



# print(dir())
'''
学习这四个内置变量，__name__,__package__,__doc__,__file__
'''
print('name:'+__name__)
print('package:'+(__package__ or'当前模块没有包'))
print('doc:'+__doc__)
print('file:'+__file__)



