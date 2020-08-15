from c2 import Person
class Student(Person):
    def __init__(self,school):
        self.school=school
    def eat(self):
        super(Student,self).eat()
        print('这是子类的实例方法')
stu1=Student('对垟小学')
stu1.eat()
# print(type(stu1))
# print(Student.total)
# print(stu1.total)
# print(stu1.name)
# print(stu1.add())


