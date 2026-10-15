# UI 自动化测试 Demo

基于 **Python + Selenium + pytest + Allure** 的 UI 自动化测试示例，以百度搜索为被测对象，演示如何用 POM（Page Object Model）设计模式组织自动化代码。

## 环境准备

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 安装 Chrome 浏览器及与浏览器版本匹配的 ChromeDriver
#    Selenium 4.6+ 已内置 Selenium Manager，通常无需手动下载 Driver
```

## 目录结构

```text
ui-automation/
├── conftest.py                       # pytest 公共 fixture（浏览器驱动的初始化与关闭）
├── requirements.txt                  # 依赖清单
├── pages/
│   └── baidu_page.py                 # 百度首页页面对象（POM）
└── testcases/
    └── test_baidu_search.py          # 百度搜索测试用例
```

## 运行方式

```bash
# 进入 ui-automation 目录
cd ui-automation

# 运行全部用例（会自动弹出 Chrome 执行）
pytest testcases/ -v

# 生成 Allure 测试报告
pytest testcases/ --alluredir=./reports
allure serve ./reports
```

## 用例设计说明

| 用例 | 场景类型 | 设计方法 | 验证点 |
| --- | --- | --- | --- |
| test_search_valid_keyword | 正常场景 | 场景法 | 结果页标题含关键词、搜索框回显输入 |
| test_search_long_keyword | 边界场景 | 边界值（38 字符） | 正常发起搜索、URL 带 wd 参数 |
| test_search_special_chars | 异常场景 | 等价类（特殊字符） | 系统不崩溃、正常响应并发起搜索 |

> 说明：用例实际执行时需以被测系统真实行为为准。百度首页"搜索框为空点击搜索"会跳转
> 到随机推荐热搜，结果不稳定，不适合做自动化断言，因此异常场景改用**特殊字符输入**
> 来验证系统对异常数据的鲁棒性，断言更稳定、可复现。

## 设计要点

- **POM 设计模式**：元素定位与业务操作封装在 `pages/baidu_page.py`，用例与页面解耦，便于维护
- **fixture 复用**：`conftest.py` 中以 `scope="class"` 管理浏览器生命周期，用例间复用实例
- **显式等待**：使用 `WebDriverWait` + `expected_conditions` 等待页面状态，避免固定 sleep
- **Allure 注解**：`@allure.feature / story / title / step` 让测试报告结构清晰、可读性强
