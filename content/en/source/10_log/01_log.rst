Log
=====
Release Date: 2021.10.23

Management Server
------------------------
- Add the message center
- Add agent threshold configuration
- Add agent registration time and startup time display
- Add Agent alias
- Bug fixs

Java Agent
--------------
- Add JVM Parameter ``-Dproject.create=true`` or ``-Dproject.create=false`` for auto create project in iast.io
- The agent pulls the CPU threshold for automatic fusing from the server
- Agent reports the time it takes to start
- Fix the bug of CPU usage shows negative numbers in Windows system
- Reduce static variables and methods, reduce the space occupied by MetaSpace
- Remove dockerfile
- Split maven module ``dongtai-servlet`` to ``dongtai-jakarta-api``,  ``dongtai-servlet-api``, ``dong-spring-api```
- Close issue HXSecurity/DongTai#280

Python Agent
---------------