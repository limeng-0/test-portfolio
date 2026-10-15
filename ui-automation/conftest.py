import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def driver():
    """浏览器驱动 fixture：测试类开始前启动浏览器，结束后统一关闭。

    scope="class" 表示同一个测试类中的用例复用同一个浏览器实例，
    减少重复启动浏览器的开销。
    """
    chrome_options = Options()
    # 启动时最大化窗口
    chrome_options.add_argument("--start-maximized")
    # 关闭"Chrome 正受到自动测试软件的控制"提示
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-automation"]
    )
    chrome_options.add_experimental_option("useAutomationExtension", False)
    # 规避部分网站对 Selenium 的自动化检测
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    # 无头模式：在无桌面环境（如 CI）中可取消下面注释，不弹出浏览器窗口
    # chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=chrome_options)
    # 隐藏 navigator.webdriver 特征，降低被反爬识别的概率
    driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"},
    )
    driver.implicitly_wait(10)  # 隐式等待，定位元素时最多等待 10 秒
    yield driver
    driver.quit()
