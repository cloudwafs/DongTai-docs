Agent Configuration
========================
Parameter table
+++++++++++++++++

- **debug**

.. list-table::
   :widths: 4 20
   :header-rows: 1
   :width: 100%

   * - Attribute
     - Value
   * - Activation
     - Add ``-Ddebug=<true or false>`` and then restart the application service
   * - Parameter Type
     - Boolean
   * - Source
     - Command line argument
   * - Variables
     - ``true`` ｜ ``false``
   * - Default
     - false
   * - Description
     - Once the debug mode is enabled, it will automatically check the scan engine is exist in the local temp folder, the scan engine will be loaded and started

- **project.name**

.. list-table::
   :widths: 4 20
   :header-rows: 1
   :width: 100%

   * - Attribute
     - Value
   * - Activation
     - Add ``-Dproject.name=<application name>`` and then restart the application service
   * - Parameter Type
     - String
   * - Source
     - Settings file
   * - Variables
     - Less than 20 characters which included: Chinese characters, uppercase/lowercase letter, digit and symbol
   * - Default
     - Demo Project
   * - Description
     - Application name

- **iast.mode**

.. list-table::
   :widths: 4 20
   :header-rows: 1
   :width: 100%

   * - Attribute
     - Value
   * - Activation
     - Add ``-Diast.mode=<hunter or normal>`` and then restart the application service
   * - Parameter Type
     - String
   * - Source
     - Settings file
   * - Variables
     - ``hunter`` ｜ ``normal``
   * - Default
     - normal
   * - Description
     - Hunter mode can coverage more vulnerabilities detection but it has a high false-positive rate and normal mode is vice versa.

- **iast.server.mode**

.. list-table::
   :widths: 4 20
   :header-rows: 1
   :width: 100%

   * - Attribute
     - Value
   * - Activation
     - Add ``-Diast.server.mode=<local or remote>`` and then restart the application service
   * - Parameter Type
     - String
   * - Source
     - Settings file
   * - Variables
     - ``local`` ｜ ``remote``
   * - Default
     - remote
   * - Description
     - Local mode support single and multiple selected vulnerabilities verify. It also can show POST Requests, Stain Source, Taint Source and etc

- **iast.proxy.enable**

.. list-table::
   :widths: 4 20
   :header-rows: 1
   :width: 100%

   * - Attribute
     - Value
   * - Activation
     - Add ``-Diast.proxy.enable=<true or false>`` and then restart the application service
   * - Parameter Type
     - Boolean
   * - Source
     - Settings file
   * - Variables
     - ``true`` ｜ ``false``
   * - Default
     - false
   * - Description
     - Enable/Disable HTTP proxy setting

- **iast.proxy.host**

.. list-table::
   :widths: 4 20
   :header-rows: 1
   :width: 100%

   * - Attribute
     - Value
   * - Activation
     - Add ``-Diast.proxy.host=<ip>`` and then restart the application service
   * - Parameter Type
     - String
   * - Source
     - Settings file
   * - Variables
     - IP address format
   * - Default
     - null
   * - Description
     - HTTP proxy server IP address

- **iast.proxy.port**

.. list-table::
   :widths: 4 20
   :header-rows: 1
   :width: 100%

   * - Attribute
     - Value
   * - Activation
     - Add ``-Diast.proxy.port=<port>`` and then restart the application service
   * - Parameter Type
     - String
   * - Source
     - Settings file
   * - Variables
     - Port format, ranging from 1 to 65535
   * - Default
     - 80
   * - Description
     - HTTP proxy server port

- **iast.service.report.interval**

.. list-table::
   :widths: 4 20
   :header-rows: 1
   :width: 100%

   * - Attribute
     - Value
   * - Activation
     - Add ``-Diast.service.report.interval=<60000>`` and then restart the application service
   * - Parameter Type
     - Integer
   * - Source
     - Settings file
   * - Variables
     - Any integer numeric
   * - Default
     - 60000
   * - Description
     - Time interval setting of sending report. Unit: ms 

- **iast.service.relay.interval**

.. list-table::
   :widths: 4 20
   :header-rows: 1
   :width: 100%

   * - Attribute
     - Value
   * - Activation
     - Add ``-Diast.service.replay.interval=<300000>`` and then restart the application service
   * - Parameter Type
     - Integer
   * - Source
     - Settings file
   * - Variables
     - Any integer numeric
   * - Default
     - 30000
   * - Description
     - Time interval setting of relay. Unit: ms 

- **iast.engine.delay.time**

.. list-table::
   :widths: 4 20
   :header-rows: 1
   :width: 100%

   * - Attribute
     - Value
   * - Activation
     - Add ``-Diast.engine.delay.time=<10>`` and then restart the application service
   * - Parameter Type
     - Integer
   * - Source
     - Settings file
   * - Variables
     - Any integer numeric
   * - Default
     - 10
   * - Description
     - Automatic (Delayed Start) agent service. Unit: sec

- **iast.dump.class.enable**

.. list-table::
   :widths: 4 20
   :header-rows: 1
   :width: 100%

   * - Attribute
     - Value
   * - Activation
     - Add ``-Diast.proxy.enable=<true or false>`` and then restart the application service
   * - Parameter Type
     - Boolean
   * - Source
     - Settings file
   * - Variables
     - ``true`` ｜ ``false``
   * - Default
     - false
   * - Description
     - Enable/Disable dump modified

- **iast.dump.class.path**

.. list-table::
   :widths: 4 20
   :header-rows: 1
   :width: 100%

   * - Attribute
     - Value
   * - Activation
     - Add ``-Diast.dump.class.path=</tmp/iast-class-dump/>`` and then restart the application service
   * - Parameter Type
     - String
   * - Source
     - Settings file
   * - Variables
     - Any path with access permission granted
   * - Default
     - /tmp/iast-class-dump/
   * - Description
     - Dump class path

- **iast.server.url**

.. list-table::
   :widths: 4 20
   :header-rows: 1
   :width: 100%

   * - Attribute
     - Value
   * - Activation
     - Add ``-Diast.server.url=<https://openapi.iast.io>`` and then restart the application service
   * - Parameter Type
     - String
   * - Source
     - Settings file
   * - Variables
     - URL Format
   * - Default
     - https://openapi.iast.io
   * - Description
     - Server URL

- **iast.allhook.enable**

.. list-table::
   :widths: 4 20
   :header-rows: 1
   :width: 100%

   * - Attribute
     - Value
   * - Activation
     - Add ``-Diast.allhook.enable=<true or false>`` and then restart the application service
   * - Parameter Type
     - Boolean
   * - Source
     - Settings file
   * - Variables
     - ``true`` ｜ ``false``
   * - Default
     - false
   * - Description
     - Enable/Disable all hook reference

- **project.create**

.. list-table::
   :widths: 4 20
   :header-rows: 1
   :width: 100%

   * - Attribute
     - Value
   * - Activation
     - Add ``-Dproject.create=<true or false>`` and then restart the application service
   * - Parameter Type
     - Boolean
   * - Source
     - Settings file
   * - Variables
     - ``true`` ｜ ``false``
   * - Default
     - false
   * - Description
     - Enable/Disable to auto create application.

- **project.version**

.. list-table::
   :widths: 4 20
   :header-rows: 1
   :width: 100%
   
   * - Attribute
     - Value
   * - Activation
     - Add ``-Dproject.version=<v1.1.0>`` and then restart the application service
   * - Parameter Type
     - String
   * - Source
     - Settings file
   * - Variables
     - Application version
   * - Default
     - v1.0
   * - Description
     - Enable to auto create application version.

- **response.length**

.. list-table::
   :widths: 4 20
   :header-rows: 1
   :width: 100%
   
   * - Attribute
     - Value
   * - Activation
     - Add ``-Dresponse.length=<1000>`` and then restart the application service
   * - Parameter Type
     - String
   * - Source
     - Settings file
   * - Variables
     - Integer > 0
   * - Default
     - None
   * - Description
     - Modify the response length from HTTP collected by Agent.

Use Case
+++++++++
.. Note:: 
    Demo Sample: SpringDemo

- Setting up the SpringDemo application to DongTai IAST with the following line:
    
.. code-block:: bash
    
    java -javaagent:/path/to/agent.jar -Dproject.name=SpringDemo -jar SpringDemo.jar

- Non-first time setting up the application/Troubleshooting the agent error message with the following line:

.. code-block:: bash

    java -javaagent:/path/to/agent.jar -Ddebug.name=true -jar SpringDemo.jar

- Automatic (Delayed Start) DongTai IAST agent with the following line (demo sample: 15 sec):

.. code-block:: bash

    java -javaagent:/path/to/agent.jar -Diast.engine.delay.time=15 -jar SpringDemo.jar

- Enable to check or troubleshooting the dump file in folder ``/tmp/class`` with the following line:

.. code-block:: bash

    java -javaagent:/path/to/agent.jar -Diast.dump.class.enable=true -Diast.dump.class.path=/tmp/class -jar SpringDemo.jar

- Enable HTTP proxy for network access with the following line (demo sample: proxy server address 10.100.100.1:80):

.. code-block:: bash

    java -javaagent:/path/to/agent.jar -Diast.proxy.enable=true -Diast.proxy.host=10.100.100.1 -Diast.proxy.host=80 -jar SpringDemo.jar

- Switch the security scanning mode between hunter mode and normal mode with the following line (Hunter mode is suggested for code review and normal mode is suggested for enterprise vulnerabilities detection):

.. code-block:: bash

    java -javaagent:/path/to/agent.jar -Diast.mode=hunter/normal -jar SpringDemo.jar

