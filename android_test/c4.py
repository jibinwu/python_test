import json
a,b,c=True,False,2
s1=json.dumps(a)
s2=json.dumps(b)
s3=json.dumps(c)
print(s1)
print(s2)
print(type(s3))
# print(type(b))