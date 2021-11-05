v1.1.0 Release Note
=======================
Release Date: 2021.11.05

Management Server
------------------------
**FEATURES**

- Add the message center

- Add agent threshold configuration

- Add agent registration time and startup time display

- Add Agent alias

- Bug fixs

Java Agent
--------------
**FEATURES**

- Add agent startup parameter: automatically create project version -Dproject.version=<v1.1.0>

- Add agent startup parameter: Configure the length of the response body obtained by the agent -Dresponse.length=<1000>. This function supports Server configuration in the next version

- Eclipse plug-in is open source: https://github.com/HXSecurity/DongTai-Plugin-Eclipse

**FIXED**

- Fix some bugs where SQL injection vulnerabilities cannot be checked out: https://github.com/HXSecurity/DongTai/issues/253

- Fix the bug that parameters cause SSRF false positives: https://github.com/HXSecurity/DongTai/issues/134

- Fix the bug that the application log cannot be displayed after installing the probe: https://github.com/HXSecurity/DongTai/issues/315

- Solve the exception report of attach mode: https://github.com/HXSecurity/DongTai/issues/321

Python Agent
---------------
**FEATURES**

- Agent pause/start by DongTai server

- Agent pause/start based on system resource usage

- Use environment variable AUTO_CREATE_PROJECT=1 for auto create project

- Report Agent startup time

- Add Reflected XSS detection

- Add XXE detection

- Add SSRF detection

**BUGFIXES**

- Fix report data parameterclassName to fully named class name

- Fix report data request/response body format

- Fix streaming response processing

- Fix response body processing

- Fix Django request form data processing

- Fix missing kwargs parameter for taint data

- Fix invalid tainted data in method pool

- Fix incorrect filter of tainted data

**BUILD**

- Auto upload package to Aliyun OSS by Github actions

- Add vulnerability testing Github actions

**TESTING**

- Add vulnerability testing script

PHP Agent
------------
**FEATURES**

- Upload collected data to Server