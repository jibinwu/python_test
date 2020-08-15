import  re
# a=' c|c++|| java|python|js '
# print(a)
# b=a.lstrip()
# c=a.strip()
# d=re.split(r'[\s\|]+',a.strip())
# print(b.split('|'))
# b=a.split('|')
# print(b)
# print(c)
# print(d)
# ll='ccppjavapythonaaaapython'
# print(ll.index('python'))


# a='c1java2cpp3python4'
# a=['aa','vv',1,'java',2]
# for i in a:
#     if i.isdigit():
#         print(i)
#     else:
#         continue
# pa=re.compile('\d')
# result1=pa.match(a)
# result2=pa.search(a)
# result=pa.findall(a)
# print(result1)
# print(result2)
# print(result)

# s='abc,acc,adc,aec,afc,ahc'
# pa=re.compile('a[^cf]c')
# result=pa.findall(s)
# print(result)

# a='python 1111Java678php'
# print(re.findall('\d',a))
# print(re.findall('\D',a))
# print(re.findall('\s',a))
# print(re.findall('[a-zA-Z]+',a,re.I))
# print(re.findall('[a-z]{3,6}?',a,re.I))


# a='pytho1python2pythonnn3'
# print(re.findall('python{1,2}',a))


# s='21  day python'
# print(s[:])
# print(s[::-1])
# s=[21,'day','python']
# print(s[::-3])
# s[1]='may'
# print(s[1])
# s[1:2]='may'
# s[1]=['may']
# print(s)

a='life is short,i use python'
b=re.findall('life(.*)python',a)
print(b)
# c=re.match('life(.*)i(.*)python',a)
# print(c.group())
# print(c.group(0))
# print(c.group(0,1,2))
# print(c.groups())
# result=re.search('life(.*)i(.*)python',a)
# print(result.group(0,1,2))


