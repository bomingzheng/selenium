import unittest
from page_class.login_page_test import LoginPage
from selenium import webdriver
from page_class.index_page_test import IndexPage
from page_class.investor_page_test import BindPage
import warnings
from data_test import common_data as CD
from data_test.login import login_data as LD
from data_test.bind import test_bid_data as BD
from data_test.bind.test_bind_element import GrabBind as GD
from ddt import ddt, data
import time
from page_class.user_page_test import UserPage
import pytest


@pytest.mark.usefixtures("bind_setup")
@pytest.mark.usefixtures("bind_teardown")
class Test(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     warnings.simplefilter("ignore", ResourceWarning)
    #     cls.wb = webdriver.Firefox()
    #     cls.wb.get(CD.web_url)
    #     cls.wb.maximize_window()
    #     LoginPage(cls.wb).login(LD.win_data['user'], LD.win_data['pwd'])
    #     IndexPage(cls.wb).choose_one()
    #     cls.ix = BindPage(cls.wb)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     # 用例执行后关闭窗口
    #     cls.wb.quit()
    #
    # def tearDown(self):
    #     self.wb.refresh()
    #     time.sleep(1)

    # 金额填写不符合
    @data(*BD.failed_bid)
    def test_invest(self, i):
        doc = '获取用户余额'
        before_money = self.ix.get_ele_attribute(GD.money_input_box, doc)
        self.ix.investment_input(i['amount'])
        # 断言
        error_msg = self.ix.get_window_error_msg()
        # 刷新页面
        self.wb.refresh()
        # 查看投资前后金额是否相等
        later_money = self.ix.get_ele_attribute(GD.money_input_box, doc)
        # 断言
        assert error_msg == i['expect']
        assert before_money == later_money

    # 成功投标
    @pytest.mark.webtest
    def test_invest_triumph(self):
        # 获取输入框用户余额
        before_money = self.ix.get_uer_money()
        # 输入投标金额100
        self.ix.investment_input(BD.succeed_bid['amount'])
        # 点击查看激活按钮按钮
        self.ix.click_win_activate()
        # 查看余额
        later_money = UserPage(self.wb).get_user_money()
        # 断言
        assert BD.succeed_bid['amount'] == int(float(before_money) - float(later_money))


if __name__ == '__main__':
    unittest.main()
