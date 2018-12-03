# coding = utf-8
from framework.base_page import BasePage


class LoginPage(BasePage):
    # 登录名输入框
    input_empspell = 'xpath=>//*[@id="J-input-user"]'
    # 登录密码输入框
    input_emppassword = 'xpath=>//*[@id="J-input-password"]'
    # 验证码输入框
    input_captcha = 'xpath=>//*[@id="J-input-captcha"]'
    # 登录按钮
    login_button = 'xpath=>//*[@id="J-login-btn"]'
    # 登录失败弹窗
    login_error = "xpath=>/html/body/div[2]/div/div/form/div[1]/span"
    # # 用户名为空提示
    # null_empspell = "xpath=>.//*[@id='app']/div/div[2]/form/div[1]/div/div[2]"
    # # 密码为空提示
    # null_emppassword = "xpath=>.//*[@id='app']/div/div[2]/form/div[2]/div/div[2]"

    def type_empspell(self, text):
        self.type(self.input_empspell, text)

    def clear_empspell(self):
        self.clear(self.input_empspell)

    def type_emppassword(self, text):
        self.type(self.input_emppassword, text)

    def clear_emppassword(self):
        self.clear(self.input_emppassword)

    def type_captcha(self, text):
        self.type(self.input_captcha, text)

    def click_login_button(self):
        self.click(self.login_button)

    def get_text(self):
        self.text(self.login_error)
