v1.0.6版本升级日志
=====================
发行日: 2021.10.23

检测能力
-------------
- 增加HTTP响应头中相关配置的安全风险检测

洞态 IAST Server 端
------------------------
**功能**

- 增加CPU阈值设置功能，Agent可根据设置值自动启停
- 增加Agent注册时可自动创建项目功能
- 增加Agent别名修改功能
- 增加消息中心
- 搜索功能，增加时间筛选字段、增加“包含”、“不包含”两种匹配逻辑

**优化**

- 修复报告导出bug
- 修复项目名无法修改bug
- 优化修改密码等页面
- 优化引擎管理，增加Agent注册时间与启动时间展示

Java Agent
--------------
- 添加 agent 启动参数 ``-Dproject.create=true`` 或 ``-Dproject.create=false`` 用于在 ``iast.io`` 自动创建项目
- agent 从服务器拉取自动熔断的CPU阈值
- agent 报告启动所需的时间
- agent 减少静态变量和方法，减少 MetaSpace 占用空间
- 删除 dockerfile
- 规范OpenAPI接口的数据格式 https://github.com/HXSecurity/DongTai/issues/280
- 解决Java Agent 启动时出现死锁 https://github.com/HXSecurity/DongTai/issues/300
- Java Agent 添加了对 JDK 17/18 的支持 https://github.com/HXSecurity/DongTai/issues/301

Python Agent
---------------
- 增加启动脚本 ``dongtai-cli``, 使用脚本启动时 agent 会自动更新
- 从 openapi 拉取策略规则
- 修改数据上报参数
- 污点数据异步上报
- 心跳增加等待上报计数
- 修复 agent 名字格式化
- 修复 windows 环境变量读取