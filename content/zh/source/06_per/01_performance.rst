DongTai IAST 性能测试
====================================
Java 代理
-----------
测试环境
++++++++++++++++++

.. list-table::
   :widths: 4 20
   :width: 100%

   * - 代理版本
     - DongTai-java-agent v1.0.4
   * - 靶场
     - DongTai-JavaAgent-Benchmark
   * - 硬件配置
     - 2 Intel Core, 8 GB memory
   * - 软件配置
     - MySQL v5.7, Redis v6.2.5, Jmeter v5.4.1


测试
++++++++++++++++
.. Note::
    
    测试用例： ``DongTai-JavaAgent-Benchmark``
    
    此用列包含 ``Spring Boot``, ``Spring MVC``, ``JDBC Template`` 和 ``Redis Template``。

    测试接口会单次查询 MySQL 和多次查询并插入 Redis 数据。

- 并发量: ``25``, ``50``, ``100``

- 测试场景: 未插桩/插桩代理的应用运行

- 测试标准: ``平均响应时间``, ``响应中位数``, ``CPU 占用率`` and ``Memory 占用率``

- 测试脚本:

.. code-block:: bash
    
    #使用 jmeter 对各种并发场景进行测试，生成测试报告
    jmeter -n -t path/to/jmeter.jmx -l agent.jtl -e -o path/to/result  



结果
+++++++
- 并发量: ``25``

  .. image:: ../_static/06_per/25.png
  

- 并发量: ``50``


  .. image:: ../_static/06_per/50.png
 


- 并发量: ``100``


  .. image:: ../_static/06_per/100.png



结论
+++++++++++


- 洞态 IAST **轻代理、重服务器** 的架构，代理只负责采集和发送数据，服务器则负责分析与识别漏洞, 并发量增高时，代理对 CPU 和 Memory 的性能影响几乎可以忽略不计。

- 洞态 IAST 的理念是构建高效 DevSecOps 流程，主要用于 **开发环境** 和 **测试环境** 即只需单次访问即可实行安全检测，并不适用在并发量高的生产环境。