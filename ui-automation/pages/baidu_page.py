from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaiduPage:
    """百度首页页面对象（Page Object Model）。

    将页面元素定位与操作封装在一处，测试用例只调用方法，
    当页面元素变化时只需修改本文件，便于维护。

    说明：百度新版首页已将搜索框升级为 <textarea id="chat-textarea">、
    按钮为 <button id="chat-submit-button">；旧版 input#kw 仍保留在
    页面中但处于隐藏状态，因此这里统一定位可见的新元素。
    """

    HOME_URL = "https://www.baidu.com"

    # 元素定位器（统一管理，便于维护）
    SEARCH_INPUT = (By.ID, "chat-textarea")
    SEARCH_BUTTON = (By.ID, "chat-submit-button")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        """打开百度首页。"""
        self.driver.get(self.HOME_URL)

    def _search_input(self):
        """等待搜索框可见且可交互后返回。"""
        return self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )

    def _search_button(self):
        """等待搜索按钮可点击后返回。"""
        return self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )

    def input_keyword(self, keyword):
        """在搜索框输入关键词。"""
        search_input = self._search_input()
        search_input.click()
        search_input.clear()
        search_input.send_keys(keyword)

    def click_search(self):
        """点击"百度一下"按钮。"""
        self._search_button().click()

    def search(self, keyword):
        """完整搜索动作：输入关键词并点击搜索。"""
        self.input_keyword(keyword)
        self.click_search()

    def get_input_value(self):
        """获取搜索框当前内容（首页与结果页均可调用）。"""
        return self._search_input().get_attribute("value")

    def get_title(self):
        """获取当前页面标题。"""
        return self.driver.title
