import json

name_emb = {'a': '1111', 'b': '2222', 'c': '3333', 'd': '4444'}
name_emb2 = ['1111', '2222', '3333',  '4444']

jsObj = json.dumps(name_emb2)
print(jsObj)
print(type(jsObj))