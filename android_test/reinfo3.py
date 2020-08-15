import unittest
import time
import HTMLTestRunner
import reinfo2

# suite=unittest.TestSuite()
# suite.addTest(reinfo2.MyTestCase("test_getReInfo1"))
# suite.addTest(reinfo2.MyTestCase("test_getReInfo2"))
# suite.addTest(reinfo2.MyTestCase("test_getReInfo3"))
now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
filename=r'D:\report'+now+'result.html'
f=open(filename,'wb')
suite=unittest.TestLoader().loadTestsFromTestCase(reinfo2.MyTestCase)
mysuite=unittest.TestSuite(suite)
runner=HTMLTestRunner.HTMLTestRunner(
    stream=f,
    title='获取续保接口测试报告',
    description='用例执行情况:'
)
runner.run(suite)
f.close()
