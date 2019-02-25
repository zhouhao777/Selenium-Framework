# coding=utf-8
import time
import unittest
from testsuites.common import login_helper
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from pageobjects.mfw_login import Login


class MfwLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def setUp(self):
        login_helper.LoginHelper.h5_login(self.driver)

    def test_login(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """

        self.driver.get("https://m.tt.ab/sales/activity/ticket/week")
        time.sleep(2)
        # BasePage.get_windows_img()  # 调用基类截图方法
        self.assertIn('门票大减价', self.driver.title)

        # try:
        #     print(self.driver.title)
        #     self.assertIn('旅游攻略',self.driver.title) # 调用页面对象继承基类中的获取页面标题方法
        #     print('Test Pass.')
        # except Exception as e:
        #     print('Test Fail.', format(e))


if __name__ == '__main__':
    unittest.main()