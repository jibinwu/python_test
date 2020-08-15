pos=0
def go(step):
    global pos
    new_pos=pos+step
    pos=new_pos
    return pos
print(go(2))
print(go(3))

'''问题：一个人开始的位置在0的位置，第一次走了2步，第二次走了3步，求这个人现在在哪个位置？
一种用非闭包解决使用global关键字，另一种用闭包解决使用nonlocal关键字
'''
def outer():
    pos=0
    def inner(step):
        nonlocal pos
        new_pos=pos+step
        pos=new_pos
        return pos
    return inner
f=outer()
print(f(2))
print(f(3))
