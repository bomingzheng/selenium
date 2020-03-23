import pytest
from page_class.login_page_test import LoginPage
from selenium import webdriver
from data_test import common_data as CD
from data_test.login import login_data as LD
import warnings
from page_class.index_page_test import IndexPage
from page_class.investor_page_test import BindPage


wb = None    # 全局变量，其他函数也可使用


# 声明是一个fixture
@pytest.fixture(scope="class")
def access_web():
    global wb
    # 前置条件
    warnings.simplefilter("ignore", ResourceWarning)
    wb = webdriver.Firefox()
    wb.get(CD.web_url)
    lg = LoginPage(wb)
    # 代表前置条件和后置条件的分割线，后面跟的是要返回的数据，可以是列表和元组
    yield (wb,lg)
    # 后置条件
    wb.quit()


@pytest.fixture()
def log_teardown():
    global wb
    # 前置条件
    yield
    # 后置条件
    wb.refresh()


@pytest.fixture(scope='class')
def bind_setup():
    global wb
    # 前置条件
    warnings.simplefilter("ignore", ResourceWarning)
    wb.get(CD.web_url)
    wb.maximize_window()
    LoginPage(wb).login(LD.win_data['user'], LD.win_data['pwd'])
    IndexPage(wb).choose_one()
    ix = BindPage(wb)
    yield (wb,ix)
    wb.quit()


@pytest.fixture()
def bind_teardown(self):
    yield
    wb.refresh()

