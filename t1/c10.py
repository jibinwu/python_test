import unittest
import os


class   TestMethod(unittest.TestCase):
    # 定义一个类，继承自unittest.TestCase
    # 每次执行用例前执行setUp()，可以在这里做一些初始化的工作
    @classmethod
    def setUp(self):

        print('setUp')

    # 每次执行用例后执行tearDown
    @classmethod
    def tearDown(self):
        print('tearDown')

    def test001(self):  # unittest中的用例必须以test开头
        print('test001')

    def test002(self):
        print('test002')


if __name__ == '__main__':
    unittest.main(verbosity=2)
# print(os.path.getctime(__file__))
print(os.path.getmtime(__file__))

