from public_page_class.test_base_page import BasePage
from data_test.bind.test_bind_element import GrabBind as BD


class UserPage(BasePage):
    def get_user_money(self):
        # 等待元素出现
        self.wait_visible(BD.user_money, doc='个人余额页面')
        # 获取可用资产元素的文本
        ele = self.get_element_text(BD.user_money)
        # 把金额单位元截取
        return ele.strip('元')
