# a='studen\ntfafa\tfafafa '
# print(a)
# a1=r'studen\ntfafa\tfafafa '
# print(a1)
# a2='''aaaaaaaaaaa\naaaaaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaaaa\naaaaaaaa'''
# print(a2)
# print('''aaaaaaaaaaaaa
# ...aaaaaaaaaaaaaaaaaaa
# ...aaaaaaaaaaaaaa''')
#
# a='ABC'
# b=a
# a='XYZ'
# print(b)
# print(ord('a '))
# print('%2d-%02d' % (34244, 142156))
# a=3.1415926
# print('提高了%f'%a)
# s1=72
# s2=85
# r=(s2-s1)
#
# a = 'abc'
# print(id(a))
# a.replace('a', 'A')
# print(id(a))

# from functools import
# a='abc'
# a.replace('a','A')
# print(a)
# max()
# a=hex(97)
# print(a)
# def add(x):
#     pass
#     # if x>0:
#     #     print('大于0')
#     # else:
#     #     print('小于0')
# a=add(2)
# print(a)
# def add(x,y):
#     return x*x,y*y
# a=add(2,3)
# print(a)
# a=[1,2]
# a.append('3')
# print(a)
# import re
# a='https://www.baidu.com/wwwindex  '
# result=re.search('www',a,re.I)
# result1=re.match('http',a,re.I)
# print(result.group())
# print(result1)

# print(a.split('/'))
# print(a.split())
# print(a.split()[0])
# print(a.strip())
# import re
# phone="2004-959-559 # 这是一个国外号码"
# r=re.findall('^\d*-\d*-\d*',phone)
# print(r[0])
import re
from bs4 import BeautifulSoup
r='<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" \
    src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">'

soup=BeautifulSoup(r,'html.parser')
# link=soup.select('img')
# print(link[0]['src'])
# print(link[0]['data-original'])

re.search('',soup)

