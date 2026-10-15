import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.baidu_page import BaiduPage


@allure.feature("百度搜索")
@allure.story("搜索功能 UI 自动化")
class TestBaiduSearch:
    """百度搜索功能 UI 自动化测试。

    用例设计方法：场景法 + 等价类 + 边界值，
    覆盖正常场景、边界场景、异常场景三类。
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """每个用例执行前重新打开百度首页，保证用例之间互不影响。"""
        self.driver = driver
        self.page = BaiduPage(driver)
        self.wait = WebDriverWait(driver, 15)
        self.page.open()

    @allure.title("正常场景：输入有效关键词后能正确搜索")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_valid_keyword(self):
        keyword = "软件测试"

        with allure.step("在搜索框输入关键词并点击搜索"):
            self.page.search(keyword)

        with allure.step("等待结果页加载，校验页面标题包含关键词"):
            self.wait.until(EC.title_contains(keyword))
            assert keyword in self.driver.title

        with allure.step("校验结果页搜索框中回显了输入的关键词"):
            assert self.page.get_input_value() == keyword

    @allure.title("边界场景：输入超长关键词系统仍能正常处理")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_long_keyword(self):
        # 边界值：输入 38 个字符，验证搜索框与系统对超长输入的处理能力
        long_keyword = "测" * 38

        with allure.step("输入 38 个字符的超长关键词并搜索"):
            self.page.search(long_keyword)

        with allure.step("校验页面正常发起了搜索（URL 带上 wd 参数）"):
            self.wait.until(EC.url_contains("wd="))
            assert "wd=" in self.driver.current_url

    @allure.title("异常场景：输入特殊字符系统不报错并能正常处理")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_special_chars(self):
        # 等价类：特殊字符属于异常输入，验证系统的鲁棒性（不崩溃、能正常响应）
        keyword = "!@#$%^&*"

        with allure.step("输入特殊字符并点击搜索"):
            self.page.search(keyword)

        with allure.step("校验系统正常发起搜索、未出现崩溃或报错（URL 带 wd 参数）"):
            self.wait.until(EC.url_contains("wd="))
            assert "wd=" in self.driver.current_url
