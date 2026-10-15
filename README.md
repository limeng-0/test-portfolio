# 软件测试实践作品集

> 本仓库收录本人在真实测试项目中沉淀的测试用例、接口测试报告、验收文档，以及接口 / UI 自动化测试代码。

## 技术栈

| 分类 | 工具 / 技术 |
| --- | --- |
| 功能测试 | 等价类划分、边界值分析、场景法、错误推测法；XMind、Excel |
| 缺陷管理 | Jira、禅道（缺陷提交、跟踪、回归闭环） |
| 接口测试 | Postman、Apifox、Jmeter；Fiddler 抓包、断点、弱网测试 |
| 自动化测试 | Python、Selenium、pytest、Allure、Requests |
| 数据库 | MySQL（多表联查、子查询、分组聚合） |
| 其他 | Linux 常用命令、Git |

## 目录结构

```text
test-portfolio/
├── test-cases/                  # 测试用例
│   ├── 攻略页面-测试用例.xlsx
│   └── 我的页面-测试用例.xlsx
├── test-reports/                # 测试报告
│   ├── APP接口集成测试报告.docx
│   └── APP用户端验收单.docx
└── ui-automation/               # UI 自动化测试代码
    ├── conftest.py
    ├── requirements.txt
    ├── pages/
    │   └── baidu_page.py
    └── testcases/
        └── test_baidu_search.py
```

## 内容说明

### 📁 test-cases/ — 测试用例

- **攻略页面-测试用例.xlsx**：App 用户端攻略页面测试用例，覆盖正常浏览、内容展示、异常分支、网络异常等场景
- **我的页面-测试用例.xlsx**：App 用户端"我的"页面测试用例，覆盖登录注册、个人中心、信息编辑等模块

用例设计方法：等价类划分、边界值分析、场景法。每条用例包含**用例编号、所属模块、前置条件、操作步骤、预期结果、优先级**等字段。

### 📁 test-reports/ — 测试报告

- **APP接口集成测试报告.docx**：基于 Apifox 的全链路接口集成测试报告，覆盖登录、下单、支付、库存扣减、退款、库存回滚等核心交易流程
- **APP用户端验收单.docx**：版本交付前的验收清单，记录各功能点验收结果、遗留问题与上线建议

### 📁 ui-automation/ — UI 自动化测试

基于 **Python + Selenium + pytest + Allure**、采用 **POM（Page Object Model）设计模式**编写的 UI 自动化示例，以百度搜索为被测对象。

- `conftest.py`：统一管理浏览器驱动的启动、反检测与生命周期
- `pages/baidu_page.py`：百度首页页面对象，封装元素定位与搜索操作
- `testcases/test_baidu_search.py`：3 条可运行用例，覆盖正常、边界、异常三类场景

| 用例 | 场景 | 设计方法 | 验证点 |
| --- | --- | --- | --- |
| test_search_valid_keyword | 正常场景 | 场景法 | 结果页标题含关键词、搜索框回显 |
| test_search_long_keyword | 边界场景 | 边界值（38 字符） | 正常发起搜索、URL 带 wd 参数 |
| test_search_special_chars | 异常场景 | 等价类（特殊字符） | 系统不崩溃、正常响应 |

运行方式：`pip install -r ui-automation/requirements.txt` 后，在 `ui-automation/` 目录执行 `pytest testcases/ -v`。

## 测试实践亮点

1. **全链路接口测试**：使用 Apifox 覆盖 登录 → 下单 → 支付 → 库存扣减 → 退款 → 库存回滚 的完整交易链路，重点验证请求参数合法性、状态码、响应数据与业务逻辑正确性
2. **接口自动化回归**：搭建接口自动化回归套件并配置定时任务，保障每次迭代版本核心链路稳定，降低回归测试工作量
3. **缺陷闭环管理**：通过 Jira 提交并跟踪缺陷，借助 Fiddler 抓包对比接口返回与页面展示，区分前后端问题边界，推动缺陷快速闭环
4. **UI 自动化实践**：使用 Selenium + pytest + Allure 落地 POM 模式，以显式等待替代固定 sleep，用 Allure 注解输出结构化报告；用例设计遵循等价类、边界值与场景法，并依据被测系统真实行为设计可稳定复现的断言

## 联系方式

- 邮箱：2799245039@qq.com

