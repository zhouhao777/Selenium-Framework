# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
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

    def test_login(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        self.driver.get('https://passport.tt.ab')
        time.sleep(2)
        login_page = Login(self.driver)
        login_page.type_passport('13200000001')
        login_page.type_password('123456')
        login_page.login_submit_btn()
        time.sleep(2)
        login_page.get_windows_img()  # 调用基类截图方法
        self.assertIn('旅游攻略', self.driver.title)

        # try:
        #     print(self.driver.title)
        #     self.assertIn('旅游攻略',self.driver.title) # 调用页面对象继承基类中的获取页面标题方法
        #     print('Test Pass.')
        # except Exception as e:
        #     print('Test Fail.', format(e))


if __name__ == '__main__':
    unittest.main()