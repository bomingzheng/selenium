from data_test.bind import test_bid_data as BD
from page_class.user_page_test import UserPage
import pytest


@pytest.mark.usefixtures("bind_setup")
@pytest.mark.usefixtures("bind_teardown")
class Test:
    # 金额填写不符合
    @pytest.mark.parametrize("i", BD.failed_bid)
    def test_invest(self, bind_setup, i):
        doc = '获取用户余额'
        # 投标前获取用户余额
        before_money = bind_setup[1].get_uer_money()
        # 投标失败
        bind_setup[1].investment_input(i['amount'])
        # 获取错误提示信息
        error_msg = bind_setup[1].get_window_error_msg()
        # 刷新页面
        bind_setup[0].refresh()
        # 提示信息是否相等
        later_money = bind_setup[1].get_uer_money()
        # 断言
        assert error_msg == i['expect']  # 提示信息是否相等
        assert before_money == later_money      # 金额是否没有发生变化

    # 成功投标
    @pytest.mark.webtest
    def test_invest_triumph(self, bind_setup):
        # 获取输入框用户余额
        before_money = bind_setup[1].get_uer_money()
        # 输入投标金额100
        bind_setup[1].investment_input(BD.succeed_bid['amount'])
        # 点击查看激活按钮按钮
        bind_setup[1].click_win_activate()
        # 查看余额
        later_money = UserPage(bind_setup[0]).get_user_money()
        # 断言
        assert BD.succeed_bid['amount'] == int(float(before_money) - float(later_money))


if __name__ == '__main__':
    pytest.main(['-s', 'test_invest.py'])

