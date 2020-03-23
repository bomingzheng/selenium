from selenium.webdriver.common.by import By


class ALLElement:

    # 手机号输入框元素
    phone = (By.XPATH, "//input[@name='phone']")

    # 密码输入框元素
    pwd = (By.XPATH, "//input[@name='password']")

    # 登录按钮元素
    login_button = (By.XPATH, "//button[text()='登录']")

    # 退出按钮
    out = (By.XPATH, "//a[contains(text(),'退出')]")

    # 否选记住手机号元素
    checkbox_phone_number = (By.XPATH, "//input[@name = 'remember_me']")

    # 免费注册
    register = (By.XPATH, "//a[contains(text(),'免费注册')]")

    # 忘记密码
    forget_pwd = (By.XPATH, "//a[text() = '忘记密码?']")

    # 登录区域的错误信息
    login_errorMsg = (By.XPATH, "//div[@class='form-error-info']")

    # 屏幕中间错误提示
    screen_wrong_bounced = (By.XPATH, "//div[@class ='layui-layer-content']")

