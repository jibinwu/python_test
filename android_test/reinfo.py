import json
import requests
s = requests.Session()  # 开启一个会话Session
jar = requests.cookies.RequestsCookieJar()   # 创建一个Cookie Jar对象
url='http://114.55.43.36:7091/api/ortherReInfo'
# headers={'authorization':'Bearer def34b98-7276-48b1-b857-fc5dae045214','Content-Type':'application/json'}
headers={'authorization':'Bearer add55b29-32af-47ea-b03d-a9ed90c30131'}
content={'plateNo':'粤J3009T'}
# r=requests.post(url,headers=headers,data=json.dumps(content))
r=requests.get(url,headers=headers,params=content)
print(r.text)
# print(r.url)
# print(r.encoding)
# print(r.content)
print(r.json())