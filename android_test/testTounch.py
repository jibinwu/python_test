import unittest
from appium import webdriver
from time import sleep
import HtmlTestRunner


class TestTounch(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9.0'
        desired_caps['deviceName'] = '9889d539424d324a4d'
        desired_caps['appPackage'] = 'com.lianxing.purchase'
        desired_caps['appActivity'] = 'com.lianxing.purchase.mall.login.LoginActivity'
        # desired_caps['noReset'] = 'True'  # 不清除数据
        # 隐藏手机键盘
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_login(self):
        self.driver.find_element_by_id("edit_username").clear()
        self.driver.find_element_by_id("edit_username").send_keys("15058321650")
        self.driver.find_element_by_id("edit_password").send_keys("jhsc8888")
        self.driver.find_element_by_id("btn_login").click()
        sleep(5)
        self.driver.find_element_by_id("btn_my").click()
        sleep(3)
        self.driver.tap([(360,2276),(672,2520)])
        sleep(2)
        self.driver.find_element_by_id("action_setting").click()
        sleep(2)
        self.driver.find_element_by_id("tv_sign_out").click()
        # self.driver.find_element_by_id("button1").click()
        # self.driver.tap([(1035,1432),(1291,1624)],500)
        # self.driver.switch_to.alert().text[0:]
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
                                              "widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                                              "android.support.v7.widget.LinearLayoutCompat/android.widget.ScrollView/"
                                             "android.widget.LinearLayout/android.widget.Button[2]").click()
        sleep(3)
        # self.driver.switch_to.alert().accept()

        # print(self.driver.switch_to.alert().text())
        # self.tounch_up(2)
        # self.driver.tap([(624,884),(816,1076)])#tap()方法不需要再加click（），已经相当于点击了
        # sleep(3)
        # self.driver.tap([(48,610),(480,1042)])
        # self.driver.switch_to_window()# 旧的  切换浏览器的窗口
        # self.driver.switch_to.window()#新的
        # self.driver.switch_to.frame()#切换嵌套的iframe

        # print(self.driver.contexts)#获取环境用的，主要用于nativeAPP和混合的webview
        # self.driver.switch_to_context()#本来这个是用来切换环境用的，现在发现竟然没有这个方法，要查下百度
        # print(self.driver.current_context)
    #实现向上滑动操作
    def tounch_up(self,n):
        size = self.driver.get_window_size()
        x1=size["width"]*0.5
        y1=size["height"]*0.75
        y2=size["height"]*0.25
        for i in range(n):
            self.driver.swipe(x1,y1,x1,y2,500)


    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="android_report",
                                                           report_title="android automation result"))





