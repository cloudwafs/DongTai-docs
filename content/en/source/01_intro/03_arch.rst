Architecture
============
High-Level Architecture
-------------------------
.. image:: ../_static/01_intro/arch.png
  :alt: arch
  :align: center

We will describe the using component and how do they work in the following.

- **DongTai IAST Client-Side Component:** 

  - ``Agent:`` Deploy alongside with the web application, use to monitor the data flow of a web application server. It will collect the data and send the data to the DongTai IAST Server via OpenAPI. The Agent will pull and apply the users’ change from the server every time after restart the web application.

- **DongTai IAST Server-Side Component:** 

  - ``Web:`` A management interface for users to manage user groups, scanned web application project, vulnerability report, agent, custom rule, etc.

  - ``WebAPI:`` Use to handle the requests from users and response the result to them.

  - ``OpenAPI:`` Use to collect data from the Client-Side Agent and storage the data into the database. It also checks the availability of the Agent by monitor the log sent back by such as heartbeat.
 
  - ``Database:`` Storage user, scanned project, report, agent’s rule, raw data collect from Agent etc.
 
  - ``Engine Task:`` Assign the analysis task to Engine.
 
  - ``Engine:`` Retrieve the task from Engine Task, it will analyze the collected data by the knowledge base of rulepack to identify vulnerability. Once the vulnerability was detected, it will store the vulnerability detail in the database and trigger notification component to notify users of the found.
 
  - ``Notification:`` A third party API used to notify users.

Architecture Diagram
---------------------

- **Diagram of Vulnerabilities Detection:** 

  :red:`A-1 ~ A-5`

  - A-1: During the regular operation or security testing, the web application will receive HTTP requests from users.

  - A-2: DongTai IAST ``Agent`` will deploy alongside the web application to monitor and collect the data from the traffic, then send the data to the DongTai IAST Server via `OpenAPI`.
 
  - A-3: Once ``OpenAPI`` received the data, it will store the data into the database and trigger ``Engine``.
 
  - A-4: ``Engine`` will start analysis the collected data from the database and the detail of the vulnerability will be stored once identified.
 
  - A-5: At the same time, users will receive notification of the vulnerability found.

- **Diagram of Management:** 

  :blue:`B-1 ~ B-4`
 
  - B-1, B-2: ``WebAPI`` will handle the request such as user group management requests, vulnerabilities reviews, etc. from users via ``Web``.
 
  - B-3, B-4: After that, ``WebAPI`` will respond to the result from the database to users and display it on ``Web``.

- **Diagram of Modify Agent Setting:** 
 
  :green:`C-1 ~ C-4`
 
  - C-1, C-2: ``WebAPI`` will handle the request from user via ``Web`` and stored the change in the database.
 
  - C-4, C-3: Once the client web application restart, Agent will pull and apply the change via ``OpenAPI``.