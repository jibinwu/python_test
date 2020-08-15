import unittest
from appium import webdriver
from time import sleep
import HtmlTestRunner
# import pytest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9.0'
        desired_caps['deviceName'] = '9889d539424d324a4d'
        desired_caps['appPackage'] = 'com.lianxing.purchase'
        desired_caps['appActivity'] = 'com.lianxing.purchase.mall.launcher.LauncherActivity'
        desired_caps['noReset']='True'#不重置数据
        #隐藏手机键盘
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    #登录和退出流程
    # def test_suceess(self):
    #     self.driver.find_element_by_id("edit_username").send_keys("15058321650")
    #     self.driver.find_element_by_id("edit_password").send_keys("jhsc8888")
    #     self.driver.find_element_by_id("btn_login").click()
    #     sleep(10)
    #     # 点击我的
    #     self.driver.find_element_by_id("btn_my").click()
    #     sleep(3)
    #     # 点击串货举报的悬浮按钮
    #     self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android."
    #                                       "widget.LinearLayout[2]/android.widget.TextView").click()
    #     #点击设置按钮
    #     self.driver.find_element_by_id("action_setting").click()
    #     sleep(3)
    #     #点击退出登录按钮
    #     self.driver.find_element_by_id("tv_sign_out").click()
    #     sleep(3)
    #     # self.driver.find_element_by_id("button1").click()
    #     #选择确定按钮退出登录
    #     self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
    #                                       "widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
    #                                       "android.support.v7.widget.LinearLayoutCompat/android.widget.ScrollView/"
    #                                       "android.widget.LinearLayout/android.widget.Button[2]").click()


        # try:
        #     if self.driver.find_element_by_id("btn_login").is_displayed():
        #         exsist=False
        #         # print("flase")
        # except Exception as e:
        #     print(e)
        #     exsist=True
        #         # print("true")
        # self.assertEqual(exsist,True)

    # def test_fail(self):
    #     self.driver.find_element_by_id("edit_username").send_keys("15058321651")
    #     self.driver.find_element_by_id("edit_password").send_keys("123456")
    #     self.driver.find_element_by_id("btn_login").click()
    #
    #
    #     try:
    #         if self.driver.find_element_by_id("btn_login").is_displayed():
    #             exsist=True
    #     except Exception as e:
    #         exsist=False
    #     self.assertEqual(exsist,True)

    #登录-首页选择商品-商品详情选择规格数量-立即购买-确认订单页面-根据是否是满赠商品去选择赠品-支付页面-输入支付密码完成支付
    def test_order(self):
        #登录
        self.driver.find_element_by_id("edit_username").clear()
        self.driver.find_element_by_id("edit_username").send_keys("15058321650")
        self.driver.find_element_by_id("edit_password").send_keys("jhsc8888")
        self.driver.find_element_by_id("btn_login").click()
        sleep(5)
        #首页选择一个商品
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
                                          "widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                                          "android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                                          "RelativeLayout/android.view.ViewGroup[2]/android.support.v7.widget."
                                          "RecyclerView/android.widget.LinearLayout[6]/android.support.v7.widget."
                                          "RecyclerView/android.widget.LinearLayout[3]").click()
        sleep(2)
        #点击立刻购买按钮
        self.driver.find_element_by_id("btn_buy").click()
        sleep(2)
        #选择规格数量，这里先选择1
        self.driver.find_element_by_id('countchange').click()
        sleep(2)
        #点击规格页面的确定按钮
        self.driver.find_element_by_id('btn_confirm').click()
        sleep(2)
        #点击商品详情页的确定按钮
        self.driver.find_elements_by_id('btn_comfirm')[0].click()
        sleep(2)
        # print(self.driver.page_source)
        # if  "com.lianxing.purchase:id/tv_choose_gift" in self.driver.page_source:
        #     #确认订单页面点击请选择赠品按钮
        #     self.driver.find_element_by_id("tv_choose_gift").click()
        #     sleep(3)
        #     #选择赠品
        #     self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
        #                                   "widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
        #                                   "android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
        #                                   "LinearLayout/android.support.v7.widget.RecyclerView/android.widget."
        #                                   "LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]"
        #                                   "/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget."
        #                                   "LinearLayout/android.widget.TextView[3]").click()
        #     sleep(3)
        #     #赠品页面点击确定按钮
        #     self.driver.find_element_by_id("btn_confirm").click()
        #     sleep(2)
        #     #再次点击提交订单按钮
        #     self.driver.find_element_by_id("btn_submit").click()
        #     sleep(2)
        #     # 点击立即支付按钮
        #     self.driver.find_element_by_id("btn_pay").click()
        #     # 输入支付密码
        #     self.driver.find_element_by_id("psd_box").send_keys("654321")
        #     sleep(3)
        # else:
        #     self.driver.find_element_by_id("btn_submit").click()
        #     sleep(2)
        #     # 点击立即支付按钮
        #     self.driver.find_element_by_id("btn_pay").click()
        #     # 输入支付密码
        #     self.driver.find_element_by_id("psd_box").send_keys("654321")
        #     sleep(3)

    #购物车下单
    def shopping_cat(self):
        self.driver.find_element_by_id("edit_username").clear()
        self.driver.find_element_by_id("edit_username").send_keys("15058321650")
        self.driver.find_element_by_id("edit_password").send_keys("jhsc8888")
        self.driver.find_element_by_id("btn_login").click()
        sleep(5)
        self.driver.find_element_by_id("btn_inventory").click()
        sleep(2)
        self.driver.find_element_by_id("btn_settlement").click()
        sleep(2)
        self.driver.find_element_by_id("btn_submit").click()
        sleep(2)
        # 确认订单页面点击请选择赠品按钮
        self.driver.find_element_by_id("tv_choose_gift").click()
        sleep(2)
        # 选择赠品
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
                                          "widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                                          "android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                                          "LinearLayout/android.support.v7.widget.RecyclerView/android.widget."
                                          "LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]"
                                          "/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget."
                                          "LinearLayout/android.widget.TextView[3]").click()
        sleep(2)
        # 赠品页面点击确定按钮
        self.driver.find_element_by_id("btn_confirm").click()

    # 登录-首页点击搜索-输入测试商品小季-选择商品。。。
    def test_search(self):
        self.driver.find_element_by_id("edit_username").clear()
        self.driver.find_element_by_id("edit_username").send_keys("15058321650")
        self.driver.find_element_by_id("edit_password").send_keys("jhsc8888")
        self.driver.find_element_by_id("btn_login").click()
        sleep(5)
        self.driver.find_element_by_id("btn_search").click()
        sleep(2)
        self.driver.find_element_by_id("edit_search").send_keys("测试商品小季")
        sleep(2)
        try:
            # if  "com.lianxing.purchase:id/search_fuzz_text_result" in self.driver.page_source:
            self.driver.find_element_by_id("search_fuzz_text_result").click()
            sleep(2)
        except  Exception as e:
            print(e)
            print("没有搜到商品")
        else:
            if self.driver.find_element_by_id("text_title").text=="测试商品小季": #这里不能写成text(),不然会报错
                self.driver.find_element_by_id("text_title").click()
                sleep(2)
                # 点击立刻购买按钮
                self.driver.find_element_by_id("btn_buy").click()
                sleep(2)
                # 选择规格数量，这里先选择1
                self.driver.find_element_by_id('countchange').click()
                sleep(2)
                # 点击规格页面的确定按钮
                self.driver.find_element_by_id('btn_confirm').click()
                sleep(2)
                # 点击商品详情页的确定按钮
                self.driver.find_elements_by_id('btn_comfirm')[0].click()
                sleep(2)
                print(self.driver.page_source)
                # if "com.lianxing.purchase:id/tv_choose_gift" in self.driver.page_source:
                #     # 确认订单页面点击请选择赠品按钮
                #     self.driver.find_element_by_id("tv_choose_gift").click()
                #     sleep(3)
                #     # 选择赠品
                #     self.driver.find_element_by_xpath(
                #         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
                #         "widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                #         "android.widget.LinearLayout/android.widget.FrameLayout/android.widget."
                #         "LinearLayout/android.support.v7.widget.RecyclerView/android.widget."
                #         "LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]"
                #         "/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget."
                #         "LinearLayout/android.widget.TextView[3]").click()
                #     sleep(3)
                #     # 赠品页面点击确定按钮
                #     self.driver.find_element_by_id("btn_confirm").click()
                #     sleep(2)
                #     # 再次点击提交订单按钮
                #     self.driver.find_element_by_id("btn_submit").click()
                #     sleep(2)
                #     # 点击立即支付按钮
                #     self.driver.find_element_by_id("btn_pay").click()
                #     # 输入支付密码
                #     self.driver.find_element_by_id("psd_box").send_keys("654321")
                #     sleep(3)
                # else:
                #     self.driver.find_element_by_id("btn_submit").click()
                #     sleep(2)
                #     # 点击立即支付按钮
                #     self.driver.find_element_by_id("btn_pay").click()
                #     sleep(2)
                #     # 输入支付密码
                #     self.driver.find_element_by_id("psd_box").send_keys("654321")
                #     sleep(3)



    def tearDown(self):
        # self.driver.find_element_by_id('setting_login_out_bt').click()
        self.driver.quit()
        sleep(3)




if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="android_report",report_title="android test report"))
