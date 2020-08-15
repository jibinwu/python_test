import re
# pi=3.1415
# a=4/3*pi*r^3
# s='AAA BBB CCC BBB'
# s1=s.replace('BBB','bbb',1)
# print(s1)




# a='Abca'
# b=re.findall('[Aa]',a)
# print(b)

# a='python'
# b=re.findall('py',a)
# print(b)


# a=re.match(r'^(\d+?)(0*)$', '102300').groups()
# print(a)
# s='1113446777'
# a=re.match('(\d{3})(\d?)(\d{2})(\d?)(\d{3})',s)
# print(a.groups())


# a=sum([1,2,3,4],10)
# print(a)

# s='pythonnnn'
# s1=re.findall('python{0,4}?',s)
# print(s1)

# re_telephone = re.match(r'^(\d{3})-(\d{3,6})$','010-12345').groups()
# print(re_telephone)

a=re.match(r'[0-9a-zA-Z]$', '.adf123')
print(a.group())

