About IAST
============
Interactive Application Security Testing (Interactive Application Security Testing) is a new application security testing program proposed by Gartner in 2012. 

IAST is equivalent to a combination of DAST and SAST, an interrelated runtime security detection technology.
It works dynamically by using an agent deployed on the web application to monitor traffic sent during runtime and analyzes traffic flow to identify security vulnerabilities in real-time. 

**IAST tools are designed to provide greater testing accuracy, and the result is clear which includes the type of vulnerability and exact location in the source code of the application. It helps developers fix risk in risks in real-time.**

.. image:: ../_static/01_intro/comparison.png
  :alt: comparison
  :align: center

.. note:: IAST is a security testing instead of scanning.

There have two main types of IAST security tools which are **active IAST** and **passive IAST**. 

- Active IAST is the approach of combines a DAST solution (web scanner) with an agent that works inside the application server.The agent will validate an existing vulnerability from the value provided by web scanner. 

- Passive IAST also requires the instrumentation of the application with an agent in the security testing environment. It will leverage any form of functional testing (input, request, database,.etc.) to collect data and deliver accurate security findings, so it doesn’t require actively running a dedicated test attack.

.. note:: DongTai IAST is a passive IAST.