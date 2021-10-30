System Context
==============

.. image:: ../_static/01_intro/context_arch.png
  :alt: concept_arch
  :align: center

**DongTai IAST consists of the following components:**

- **DongTai IAST Agent:**

  Use to monitor the data flow of a web application server. The Agent will monitor requests through code instrumentation and continuously collect data, then sends these data on to the DongTai IAST Server. 
  
  An IAST Agent would be installed on each web application server in case of multiple web applications were deployed on a single machine.
  

- **DongTai IAST Server:** 

  The main component of the DongTai IAST architecture that produces the user interface, analyzes the data collected by DongTai IAST Agents to identify vulnerabilities, stores the vulnerabilities and generates vulnerabilities reports. It also notifies users of the finding vulnerabilities, displays the result details, provides Web-APIs, manages user, group, scanned web application projects, and custom rules. 
  

**System Context Diagram of DongTai IAST:**

- During the regular operation or security testing, the web application will receive HTTP requests from users.


- DongTai IAST Agent will deploy alongside the web application to monitor and collect the data from the traffic, then send the data to the DongTai IAST Server.


- All the collected data will be analyzed on DongTai IAST Server. Once a vulnerability is detected, the server will notify users of the finding. Users also can review the report with include vulnerable lines of code, runtime data, and remediation on the management server.