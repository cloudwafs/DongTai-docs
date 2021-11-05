v1.1.0版本升级日志
=====================
发行日: 2021.11.05

检测能力
-------------


洞态 IAST Server 端
------------------------
**功能**



**优化**


Java Agent
--------------
**功能**
- 新增 agent 启动参数：自动创建项目版本 -Dproject.version=<v1.1.0>
- 新增 agent 启动参数：配置agent获取的响应体长度 -Dresponse.length=<1000>。该功能于下个版本支持Server端配置
- Eclipse 插件已开源：https://github.com/HXSecurity/DongTai-Plugin-Eclipse

**修复**
- 修复某些SQL注入漏洞无法检出的bug: https://github.com/HXSecurity/DongTai/issues/253
- 修复参数导致SSRF误报的bug: https://github.com/HXSecurity/DongTai/issues/134
- 修复安装探针后应用日志无法显示的bug: https://github.com/HXSecurity/DongTai/issues/315
- 解决 attach 模式的异常报错: https://github.com/HXSecurity/DongTai/issues/321


Python Agent
---------------


PHP Agent (Beta)
--------------------
