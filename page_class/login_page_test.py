from data_test.login.Element_locator import ALLElement
from public_page_class.test_base_page import BasePage


class LoginPage(BasePage):

    def login(self, user, pd):   # 传入用户名和密码两个参数
        doc = '登录模块'
        # 等待手机号码输入框元素可见，此处需要输入元组类型，所以直接调用元素定位
        self.wait_visible(ALLElement.phone, doc=doc)

        # 手机号码输入框输入用户名，
        self.input_keys(ALLElement.phone, user, doc)

        # 密码输入框输入的密码
        self.input_keys(ALLElement.pwd, pd, doc)

        # 点击登录按钮
        self.click_element(ALLElement.login_button, doc)

    def registry_entry(self):
        doc = '注册模块'

        self.wait_visible(ALLElement.register, doc=doc)
        # 点击注册按钮
        self.click_element(ALLElement.register, doc)

    def forget_pwd(self):
        doc = '忘记密码'
        self.wait_visible(ALLElement.forget_pwd, doc=doc)
        # 点击忘记密码按钮
        self.click_element(ALLElement.forget_pwd, doc)

    # 登录区域的错误信息
    def get_error_login_area(self):
        doc = '登录模块_输入区域错误'
        self.wait_visible(ALLElement.login_errorMsg, doc=doc)
        return self.get_element_text(ALLElement.login_errorMsg, doc)

    # 屏幕中间的错误信息
    def get_error_central(self):
        doc = '登录模块_屏幕区域错误'
        self.wait_visible(ALLElement.screen_wrong_bounced, doc=doc)
        return self.get_element_text(ALLElement.screen_wrong_bounced, doc)