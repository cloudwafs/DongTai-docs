DongTai IAST Performance Testing
====================================
Java Agent
-----------
Test Environment
++++++++++++++++++

.. list-table::
   :widths: 4 20
   :width: 100%

   * - Agent
     - DongTai-java-agent v1.0.4
   * - Lab
     - DongTai-JavaAgent-Benchmark
   * - Hardware
     - 2 Intel Core, 8 GB memory
   * - Software
     - MySQL v5.7, Redis v6.2.5, Jmeter v5.4.1


Implementation
++++++++++++++++
.. Note::
    
    We will use ``DongTai-JavaAgent-Benchmark`` as our test case. 
    
    It is a Spring application which include ``Spring Boot``, ``Spring MVC``, ``JDBC Template`` and ``Redis Template``.

    :green:`Single` MySQL search and :green:`Multiple` Redis search and insert will be done in this test case.

- Test Request Parameter: ``25``, ``50``, ``100``

- Test Scenario: Test Case run ``with and without`` DongTai IAST Java Agent

- Test Response: ``Average Response Time``, ``Median Response Time``, ``CPU Usage`` and ``Memory Usage``

- Test Command:

.. code-block:: bash
    
    #Using jmeter to load the test functional behaviour and generate performance result
    jmeter -n -t path/to/jmeter.jmx -l agent.jtl -e -o path/to/result  



Result
+++++++
- Concurrency Parameter: ``25``

  .. image:: ../_static/06_per/25.png
    :alt: 25

- Concurrency Parameter: ``50``

  .. image:: ../_static/06_per/50.png
    :alt: 50

- Concurrency Parameter: ``100``


  .. image:: ../_static/06_per/100.png
    :alt: 100


Conclusion
+++++++++++

- Due to the **light agent and heavy server** architecture. 
The agent is only responsible for collecting and sending data, while the server is responsible for analyzing and identifying vulnerabilities.
When the amount of concurrency increases, the effect of the agent on CPU and Memory performance is almost negligible.

- DongTai IAST is specially design to efficient the process of DevSecOps, which is mainly used in **development environment** and **test environment**. 
It only needs a single traffic to implement security detection so it was not suitable for high-concurrency production environments.