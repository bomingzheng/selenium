from data_test.bind.test_bind_element import GrabBind as GB
from public_page_class.test_base_page import BasePage
from page_class.log_class_test import MyLog
logging = MyLog()


class BindPage(BasePage):

    # 投资输入框
    def investment_input(self, money):
        doc = '投资模块'
        # 等待输入框元素出现
        self.wait_visible(GB.money_input_box, doc=doc)
        # 在输入框输入金额
        self.input_keys(GB.money_input_box, money, doc)
        self.click_element(GB.bid_button, doc)

    # 获取输入框用户余额
    def get_uer_money(self):
        doc = '获取用户余额'
        self.wait_visible(GB.money_input_box, doc=doc)
        # 获取输入空框的金额数量
        return self.get_ele_attribute(GB.money_input_box, "data-amount", doc)

    # 点击投资成功提示框的查看激活按钮
    def click_win_activate(self):
        doc = '投资成功'
        self.wait_visible(GB.view_activate, doc=doc)
        # 点击查看激活按钮
        self.click_element(GB.view_activate, doc)

    # 关闭提示框
    def click_affirm_button(self):
        doc = '投资失败_关闭弹窗'
        self.wait_visible(GB.confirm_button, doc=doc)
        # 关闭弹窗
        self.click_element(GB.confirm_button, doc)

    # 获取弹窗错误信息
    def get_window_error_msg(self):
        doc = '投资失败_错误弹窗信息'
        self.wait_visible(GB.windows_error_msg, doc=doc)
        # 获取弹窗信息
        return self.get_element_text(GB.windows_error_msg, doc)
