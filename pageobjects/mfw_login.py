#!/usr/bin/env python
#coding=utf-8
from framework.base_page import BasePage


class Login(BasePage):
    # 输入账号框,输入密码框
    passport = "xpath=>//*[@id='_j_login_form']/div[1]/input"
    password = "xpath=>//*[@id='_j_login_form']/div[2]/input"
    # 登录按钮
    login_button = "xpath=>//*[@id='_j_login_form']/div[5]/button"

    def type_passport(self, text):
        self.type(self.passport, text)

    def type_password(self, text):
        self.type(self.password, text)

    def login_submit_btn(self):
        self.click(self.login_button)
