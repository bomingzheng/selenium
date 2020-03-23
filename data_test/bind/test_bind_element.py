# 投标模块元素定位
from selenium.webdriver.common.by import By


class GrabBind:

    # 抢投标按钮
    grab_tender = (By.XPATH, "//a[text() = '抢投标']")

    # 投资输入框
    money_input_box = (By.XPATH, "//input[contains(@class,'invest-unit-investinput')]")

    # 投标按钮
    bid_button = (By.XPATH, "//button[text()='投标']")

    # 失败弹窗确认按钮
    confirm_button = (By.XPATH, "//a[text()='确认']")

    # 错误弹窗文案元素
    windows_error_msg = (By.XPATH, "//div[@class ='text-center']")

    # 查看并激活按钮元素
    view_activate = (By.XPATH, '/html/body/div[9]/div/div[1]/div[4]/button')

    # 用户余额元素
    user_money = (By.XPATH, "//li[@class='color_sub']")



