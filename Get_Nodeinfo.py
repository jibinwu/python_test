from xml.dom import minidom
# #打开xml文件
dom=minidom.parse('class_info.xml')
root=dom.documentElement#获取文档对象元素
names=root.getElementsByTagName('name')
ages=root.getElementsByTagName('age')
citys=root.getElementsByTagName('city')
for i in range(4):
    print(names[i].firstChild.data)
    print(ages[i].firstChild.data)
    print(citys[i].firstChild.data)


#读取xml属性节点
# dom=minidom.parse('class_info.xml')
# root=dom.documentElement
# logins=root.getElementsByTagName('login')
# for i in range(2):
#     username=logins[i].getAttribute('username')
#     print(username)
#     password=logins[i].getAttribute('password')
#     print(password)


# dom=minidom.parse('class_info.xml')
# root=dom.documentElement
# tag=root.getElementsByTagName('name')
# print(tag[0].nodeName)
# print(tag[0].nodeValue)
# print(tag[0].nodeType)




