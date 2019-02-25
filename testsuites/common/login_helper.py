# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.mfw_login import Login


class LoginHelper(object):
    @staticmethod
    def h5_login(driver):
        driver.get('https://passport.tt.ab')
        login_page = Login(driver)
        login_page.type_passport('xxx')
        login_page.type_password('xxx')
        login_page.login_submit_btn()
        time.sleep(2)
        # login_page.get_windows_img()  # 调用基类截图方法
        try:
            assert '旅游攻略' in driver.title  # 调用页面对象继承基类中的获取页面标题方法
            print('Login Success.')
        except Exception as e:
            print('Login Fail.', format(e))


if __name__ == '__main__':
    unittest.main()