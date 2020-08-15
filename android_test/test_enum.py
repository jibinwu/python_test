from enum import Enum
from enum import IntEnum #限制m枚举成员只能取整型或者类似整型的字符串
from enum import unique  #同一个值只能有一个枚举成员  A=1和B=1，这样是不被允许的

# @unique
# class VIP(IntEnum):
class VIP(Enum):  #枚举是单例模式，所以不能被实例化
    YELLOW='1'
    GREEN=2
    RED=3
    BLUE=3
# VIP.YELLOW=2
print(VIP.YELLOW)
print(type(VIP.YELLOW))
print(VIP.YELLOW.value)
print(VIP.YELLOW.name)
for i in VIP:
    print(i)
    print(type(i))
for i in VIP.__members__:
    print(i)
print(VIP['YELLOW'])
print(VIP("1"))
print(VIP.YELLOW is VIP.GREEN)
print(VIP.RED==VIP.BLUE)
print(VIP.RED is VIP.BLUE)


