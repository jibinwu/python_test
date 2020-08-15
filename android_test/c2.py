class Person:#类其实就是一个模板，模板可以生成很多个具体的对象
    total=0
    sex='男'
    name='qiyue'
    #一般来说，单独创建类变量是没啥意义的，但是可以创建统计生成了多少个对象的类变量是很有意义的
    def __init__(self,name,age): #可以把构造函数当成一种特殊的实例方法
        self.name=name
        self.age=age
        self.sex='女'
        # self.__class__.total+=1
        # print('当前学生总数为:'+str(self.__class__.total))
        # print(self.name)
        # print(name) #别把name和self.name混在一起，实际上print(name)打印的是形参name
#在类中，可以把变量当成是一种特征（name,age）,把方法当成是一种行为（能干什么或做什么事）
    def eat(self):
        # print(self.sex)
        # print(Person.name) #在实例方法中调用类变量第1种
        # print(self.__class__.name)#在实例方法中调用类变量第2种，实际上self.__class__等价于Person
        print('吃饭的功能')
        # print(self.homework())
        # return self.age
    def homework(self):
        print('做作业')
        return  'homework方法的返回值'
    @classmethod
    def plus_sum(cls):#不要看到方法中的参数是cls就认为是类方法，同理不要看到self就当成是实例方法，关键在于@classmethod装饰器
        # print(cls.plus_sum())
        print('对象也是可以调用类方法的')
    @staticmethod  #原则上不推荐使用静态方法，因为它和类、对象的关联性不强
    def add():
        print(Person.total)
        print('这是一个静态方法')


if __name__=='__main__':
    jbw=Person('季老师',18)
# jbw.plus_sum
    jbw.add()#对象可以访问静态方法
# Person.add()#类也可以访问静态方法

# zxy=Person('朱老师',19)
# jbw.eat()
# fun=jbw.eat()
# zxy=Person('朱老师',19)
# print(jbw.name)
# jbw.eat()
# print(jbw.eat())
# print(Person.name)