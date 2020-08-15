import requests #获取网页的内容
from bs4 import BeautifulSoup#BeautifulSoup(a,'html.parser')  soup.selec('a')    剖析网页内容(比如具体的标签内容)
# response=requests.get('http://news.sina.com.cn/china/?vt=1&wm=2281_0172')
# response.encoding='utf-8'
# response_html=response.text# html
# soup_result=BeautifulSoup(response_html,'html.parser')
# news_item=soup_result.select('.news-item') #获取div(包含标题,时间,链接)
# print(news_item[:2])
# for i in news_item:
#     title=i.select('a')[0].text
#     h_link=i.select('a')[0]['href']
#     # h_time=i.select('.time')[0].text
#     print(title,h_link)
# print(news_item)
# res_html1=BeautifulSoup(res_html,'html.parser')
# title=res_html1.select('.main-title')
# print(title[0].text)

# print(res_html1)


# a='\
# <html>\
# <body>\
# <h1 id="title">hello world</h1>\
# <a href="#" class="link">this is link1</a>\
# <a href="#link2" class="link">this is link2</a>\
# </body>\
# <html>'
# soup=BeautifulSoup(a,'html.parser')
# # header=soup.select('h1')
# alinks=soup.select('a')
# for link in alinks:
#     print(link['href'])#使用select找出所有a标签的href链接
# print(header[0].text)
# alink=soup.select('a')
# alink=soup.select('#title')#使用select找出所有id为title的元素（id前面需加#）
# alink=soup.select('.link')#使用select找出所有class为link的元素(class前需加.)
# # print(alink)
# print(header[0].text)
# print(soup)
# print(alinks)


a='\
<html>\
<body>\
<h1 id="title">hello world</h1>\
<a href="#" class="link">this is link1</a>\
<a href="#link2" class="link">this is link2</a>\
</body>\
<html>'
soup=BeautifulSoup(a,'html.parser')
result=soup.select('a')
print(result[0]['href'])
