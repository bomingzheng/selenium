from page_class.index_page_test import IndexPage
from data_test.login import login_data as LD
import pytest


@pytest.mark.usefixtures("log_teardown") # 引入类 fixture
@pytest.mark.usefixtures("access_web")   # 模块fixture，每个用力都运行所以夹在类上
class TestLogin:

    # 手机号位数不对
    @pytest.mark.parametrize("i", LD.unusual_data)
    def test_login_error_format(self,access_web, i):
        # 步骤：  在登录页面输入用户名和密码点击登录按钮
        access_web[1].login(i['user'], i['pwd'])
        # 断言    提示输入正确的用户名
        assert access_web[1].get_error_login_area() == i['except']

    # 密码错误和未注册
    @pytest.mark.parametrize("data", LD.pwd_error_data)
    def test_login_unregistered(self, access_web, data):
        access_web[1].login(data['user'], data['pwd'])
        # 断言    提示输入正确的用户名
        assert access_web[1].get_error_central() == data['except']

    # 成功登录用例
    @pytest.mark.webtest
    def test_login_win(self, access_web):  # fixture用函数名来接收返回的值，以参数形式传递调用
        # 步骤：  在登录页面输入用户名和密码点击登录按钮
        access_web[1].login(LD.win_data['user'], LD.win_data["pwd"])  # 通过传递参数取下标的方式获取值
        # 断言  把该元素存在判定封装成类然后调用，断言判断是否返回true
        assert IndexPage(access_web[0]).exists_logout()


if __name__ == '__main__':
    pytest.main(['-s', 'test_login.py'])