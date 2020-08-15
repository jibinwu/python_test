from urllib import request
import json
with  request.urlopen(r'https://api.douban.com/v2/book/2129650') as f:
    data=f.read()
        print('Status:', f.status, f.reason)
        result=json.loads(data)
    print(result)


