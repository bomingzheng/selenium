import random
from data_test.bind.test_bind_element import GrabBind
from data_test.login.Element_locator import ALLElement
from public_page_class.test_base_page import BasePage
# 为了页面数据分离，把断言和等待封装类然后调用


class IndexPage(BasePage):

    def exists_logout(self):
        doc = '登陆成功退出按钮的元素存在'
        try:
            self.wait_exit(ALLElement.out, doc=doc)

            return True
        except:
            return False

    # 选标操作(默认选择第一个抢投标按钮，元素定位时不可选会过滤掉)
    def choose_one(self):
        doc = '抢投标按钮'
        self.wait_visible(GrabBind.grab_tender, doc=doc)
        # 点击抢投标按钮
        self.click_element(GrabBind.grab_tender, doc)

    # 随机任意一个抢投标按钮
    def choose_random(self):
        doc = '抢投标按钮'
        self.wait_visible(GrabBind.grab_tender, doc=doc)
        # 使用elements返回一个列表
        eles = self.wb.find_elements(*GrabBind.grab_tender)
        # 随机选取范围从第一个小标开始，因为包含最后一个下标所以  需要-1
        i = random.randint(0, len(eles)-1)
        eles[i].click()










