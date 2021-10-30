OpenAPI 接口文档
===========================
Agent 开发流程简介
---------------------
Agent 使用过程中的全流程
+++++++++++++++++++++++++
#. 访问WEB页面，下载Agent

#. 配置Agent，启动服务

#. Agent 向 OpenAPI 服务发起 Agent 注册请求，获取 AgentID

#. Agent 向 OpenAPI 服务发起请求，获取规则，然后根据规则对服务进行信息采集

#. Agent 每分钟向 OpenAPI 服务发起一次请求，通知 Agent 存活，并拉取 需要 Agent 重放的请求，在 Agent 内部进行重放

#. Agent 启动时向 OpenAPI 服务发起请求，上报目标应用中存在的 API 接口及参数信息

#. Agent 每分钟向 OpenAPI 服务发起请求，上报目标应用使用到的依赖组件数据

#. Agent 每分钟向 OpenAPI 服务发起请求，上报目标应用处理 API 请求时产生的一系列不可信数据在内部传播的相关方法调用数据

#. Agent 每分钟向 OpenAPI 服务发起请求，上报 Agent 运行过程中产生的异常信息

Agent 开发流程
++++++++++++++
#. 开发 Agent，进行污点源方法、传播方法、危险方法、过滤方法等进行 Hook 实现参数、返回值、对象等信息的获取与唯一标识

#. 将 Hook 的逻辑与 Hook 点分开，实现 Hook 逻辑与 Hook 策略的解藕

#. 开发完成后，进行项目的对接，包括：

  #. OpenAPI 实现 Agent 下载的接口

  #. OpenAPI 实现 Agent 获取规则的接口

  #. WebAPI及WEB 实现 Agent 下载的功能、规则配置的功能

API接口地址及鉴权方式
----------------------
#. 测试服务接口地址

  *请使用本地的OpenAPI服务地址 或 测试环境 OpenAPI 服务地址，如果地址不正确，可通过公众号* 洞态 *告知我们*

.. code-block:: bash
    
    http://a28754cd66991441d8d682808caecead-626172336.cn-north-1.elb.amazonaws.com.cn:8000  


#. 内部员工测试地址

  *测试地址可能会变，如果得不到响应通过访问 iast-test.huoxian.cn 自行获取*

.. code-block:: bash
    
    http://192.168.2.161:8001


#. 接口验证方式

 *发送HTTP请求时，增加如下Header头即可，其中，custom-token可通过 Add Agent 页面进行获取*

.. code-block:: bash
    
    Authorization: Token <custom-token>

API 接口文档
-------------------
Agent 注册
+++++++++++++
``Agent`` 启动时，向 ``Server`` 端注册的接口

请求

.. code-block:: bash
    
    Authorization: Token <custom-token>

Body 参数样例

.. code-block:: bash
    
    Authorization: Token <custom-token>

Body 参数说明

.. list-table::
   :widths: 4 4 10 4 4
   :header-rows: 1
   :width: 100%
   
   * - 参数名
     - 类型
     - 描述
     - 默认值
     - 是否必须
   * - name
     - string
     - Agent 名字，规则：osName + "-" + hostname + "-" + 探针版本号 + "-" + 探针唯一ID
     - 无
     - 必须
   * - language
     - string
     - Agent 对应的语言，可选值：（JAVA、PYTHON、PHP、GO)
     - JAVA
     - 必须
   * - version
     - string
     - Agent 版本，Agent的版本号，如：v1.0.5
     - 无
     - 必须
   * - projectName
     - string
     - 配置 Agent 时指定的项目名称，各Agent测自己实现及添加对应的配置方法
     - Demo Project
     - 非必需
   * - hostname
     - string
     - Agent 所在系统的主机名
     - 无
     - 必须
   * - network
     - string
     - 所在主机的网络情况（IP地址等）
     - 无
     - 非必需
   * - containerName
     - string
     - Agent所在的容器名称（Java中的Tomcat、Python中的uwsgi、PHP中的php-fpm或Tomcat等）
     - 无
     - 非必需
   * - containerVersion
     - string
     - Agent所在的容器版本
     - 无
     - 非必须
   * - serverAddr
     - string
     - Agent所在服务的访问地址，ip地址或域名f
     - 无
     - 必须
   * - serverPort
     - string
     - Agent所在服务的端口
     - 无
     - 必须
   * - serverPath
     - string
     - 服务所在的路径
     - 无
     - 非必需
   * - serverEnv
     - string
     - 服务器中的环境变量信息，需要Base64编码
     - 无
     - 必须
   * - pid
     - string
     - 当前服务对应的进程 ID
     - 无
     - 非必需

响应体样例

.. code-block:: bash

    {
        "status": 201,
        "msg": "success",
        "data":{
            "id": "1"
        }
    }

响应体字段说明

.. list-table::
   :widths: 4 4 4 
   :header-rows: 1
   :width: 100%
      
   * - 字段名
     - 类型
     - 描述
   * - status
     - Int
     - 返回码
   * - msg
     - string
     - 错误信息
   * - data
     - []obj
     - 数据

obj 字段说明

.. list-table::
   :widths: 4 4 4 
   :header-rows: 1
   :width: 100%
   
   * - 参数名
     - 类型
     - 描述
   * - id
     - int
     - 注册之后的Agent ID

Agent 获取 HOOK 规则
++++++++++++++++++++++++
``Engine`` 运行时，从 ``OpenAPI`` 服务获取规则

请求

.. code-block:: bash

    GET /api/v1/profiles?language=<language>

Query

.. list-table::
   :widths: 4 4 10 4
   :header-rows: 1
   :width: 100%
   
   * - 参数名
     - 类型
     - 描述
     - 默认值
   * - language
     - string
     - Agent 对应的语言，可选值：（JAVA、PYTHON、PHP、GO)
     - JAVA

响应体样例

.. code-block:: bash

    {
        "status": 201,
        "msg": "success",
        "data": [
            {
                "type": 1,
                "enable": 1,
                "value": "String",
                "details": [
                    {
                        "source": "P1",
                        "track": "",
                        "target": "O",
                        "value": "java.lang.String.<init>(java.lang.String)",
                        "inherit": "false"
                    },
                    {
                        "source": "P1",
                        "track": "",
                        "target": "O",
                        "value": "java.lang.String.<init>(java.lang.StringBuffer)",
                        "inherit": "false"
                    }
                ]
            }
        ]
    }

响应体字段 - data说明

.. list-table::
   :widths: 4 4 10
   :header-rows: 1
   :width: 100%
   
   * - 字段名
     - 类型
     - 描述
   * - type
     - int
     - hook规则类型，1 - 传播方法规则、2 - 不可信数据获取方法规则、3 - 过滤方法规则、4 - 危险方法规则
   * - enable
     - int
     - 规则是否启用，1 - 启用、0 - 禁用
   * - value
     - string
     - 规则类型描述（如：Propagator:String、Sink:CMD-Injection等）
   * - details
     - []detail
     - 规则详情

Server 端启停 Agent
+++++++++++++++++++++
``Agent`` 运行时，每秒向 ``Server`` 端查询一次，根据 ``Server`` 端的控制命令 启动 或 暂停 ``Agent``

请求

.. code-block:: bash

    GET /api/v1/engine/startstop?agentName=<agentName>

Query

.. list-table::
   :widths: 4 4 10 4 4
   :header-rows: 1
   :width: 100%
   
   * - 参数名
     - 类型
     - 描述
     - 默认值
     - 是否必须
   * - agentName
     - string
     - Agent 名字，规则：osName + "-" + hostname + "-" + 探针版本号 + "-" + 探针唯一ID
     - 无
     - 否

Agent 上报数据
+++++++++++++++
``Agent`` 向 ``Server`` 端发送报告数据，包括：Agent心跳、依赖组件、方法调用数据、API接口数据、错误日志

请求

.. code-block:: bash

    POST /api/v1/report/upload


Body 参数样例

.. code-block:: bash

    {
        "detail": {
            "disk": "{}",
            "memory": "{\"total\":\"2GB\",\"rate\":0,\"use\":\"80.605MB\"}",
            "agentId": 5848,
            "cpu": "{\"rate\":32}",
            "methodQueue": 0,
            "replayQueue": 0,
            "reqCount": 0,
            "reportQueue": 49
        },
        "type": 1
    }

Body 参数说明

.. list-table::
   :widths: 4 4 10 4 4
   :header-rows: 1
   :width: 100%
   
   * - 参数名
     - 类型
     - 描述
     - 默认值
     - 是否必须
   * - type
     - int
     - 数据类型，可选择：1 - Agent心跳数据、17 - 依赖组件数据、36 - 方法调用数据、
     - 无
     - 必须
   * - detail
     - {}detail
     - 数据详情，随type不同，格式不同，将分别详细解释
     - 无
     - 必须


Agent 心跳数据格式
^^^^^^^^^^^^^^^^^^^^^^^
detail 参数样例

.. code-block:: bash

    {
        "disk": "{}",
        "memory": "{\"total\":\"2GB\",\"rate\":0,\"use\":\"80.605MB\"}",
        "agentId": 5848,
        "cpu": "{\"rate\":32}",
        "methodQueue": 0,
        "replayQueue": 0,
        "reqCount": 0,
        "reportQueue": 49
    }

detail 参数说明

.. list-table::
   :widths: 4 4 10 4 4
   :header-rows: 1
   :width: 100%
   
   * - 参数名
     - 类型
     - 描述
     - 默认值
     - 是否必须
   * - disk
     - string
     - 安装Agent服务所在服务器的磁盘使用情况
     - 无
     - 必须
   * - memory
     - string
     - 安装Agent服务所在服务器的内存使用情况
     - 无
     - 必须
   * - agentId
     - int
     - Agent ID
     - 无
     - 必须
   * - cpu
     - string
     - 安装Agent服务所在服务器的CPU使用情况
     - 无
     - 必须
   * - methodQueue
     - int
     - Agent端待发送的方法调用图数量
     - 无
     - 必须
   * - replayQueue
     - int
     - Agent端待重放的请求数量
     - 无
     - 必须
   * - reqCount
     - int
     - 安装探针的服务，接收到的API请求次数
     - 无
     - 必须
   * - reportQueue
     - int
     - Agent端待发送的报告数量
     - 无
     - 必须

依赖组件 数据格式
^^^^^^^^^^^^^^^^^^
detail 参数样例

.. code-block:: bash

    {
        "packagePath": "/Users/xxx/spring-boot/2.3.2.RELEASE/spring-boot-2.3.2.RELEASE.jar",
        "agentId": 5848,
        "packageSignature": "efd5812bc736735e71447a51701becd14c2bede0",
        "packageName": "spring-boot-2.3.2.RELEASE.jar",
        "packageAlgorithm": "SHA-1"
    }

detail 参数说明

.. list-table::
   :widths: 4 4 10 4 4
   :header-rows: 1
   :width: 100%
   
   * - 参数名
     - 类型
     - 描述
     - 默认值
     - 是否必须
   * - agentId
     - int
     - Agent ID
     - 无
     - 必须
   * - packagePath
     - string
     - 组件所在的物理路径
     - 无
     - 必须
   * - packageName
     - string
     - 组件的包名
     - 无
     - 必须
   * - packageSignature
     - string
     - 组件的方法签名
     - 无
     - 必须
   * - packageAlgorithm
     - string
     - 组件的签名计算方法，统一使用 SHA-1
     - 无
     - 必须

方法调用数据
^^^^^^^^^^^^^
detail 参数样例

.. code-block:: bash

    {
    "agentId": 5853,
    "uri": "/",
    "url": "http://localhost:8080/",
    "protocol": "HTTP/1.1",
    "contextPath": "",
    "pool": [
        {
            "invokeId": 1024,
            "interfaces": [],
            "targetHash": [1824828808],
            "targetValues": "{q=0.9}",
            "signature": "java.util.HashMap.put",
            "originClassName": "java.util.HashMap",
            "sourceValues": "q 0.9 ",
            "methodName": "put",
            "className": "java.util.Map",
            "source": false,
            "callerLineNumber": 252,
            "callerClass": "org.springframework.util.MimeTypeUtils",
            "args": "",
            "callerMethod": "parseMimeTypeInternal",
            "sourceHash": [
                1197294456,
                365502861
            ],
            "retClassName": ""
        }
    ],
    "language": "JAVA",
    "clientIp": "127.0.0.1",
    "secure": false,
    "replayRequest": false,
    "method": "GET",
    "reqHeader": "aG9zdDpsb2NhbGhvc3Q6ODA4MApj",
    "reqBody": "",
    "resBody": "<!DOCTYPE html>\n<html la",
    "scheme": "http",
    "resHeader": "SFRUUC8xLjEgMjAw"
    }

detail 参数说明

.. list-table::
   :widths: 4 4 10 4 4
   :header-rows: 1
   :width: 100%
   
   * - 参数名
     - 类型
     - 描述
     - 默认值
     - 是否必须
   * - agentId
     - int
     - Agent ID
     - 无
     - 必须
   * - protocol
     - string
     - HTTP 协议
     - 无
     - 必须，RPC请求中自行处理
   * - scheme
     - string
     - HTTP 协议
     - 无
     - 必须，RPC请求中自行处理
   * - secure
     - boolean
     - 是否为HTTPS
     - 无
     - 必须，RPC请求中为空
   * - method
     - string
     - HTTP请求方法名称，GET、POST 等
     - 无
     - 必须，RPC 请求中非必需
   * - uri
     - string
     - HTTP请求的uri
     - 无
     - 必须
   * - url
     - string
     - HTTP请求的url
     - 无
     - 必须
   * - queryString
     - string
     - HTTP请求对应的 URL 查询参数
     - 无
     - 必须，可为空
   * - contextPath
     - string
     - HTTP 请求的上下文路径
     - 无
     - 必须，可为空
   * - reqHeader
     - string
     - 请求头（HTTP/Dubbo RPC/gRPC等）
     - 无
     - 必须
   * - reqBody
     - string
     - 请求体（HTTP/Dubbo RPC/gRPC等）
     - 无
     - 必须，可为空
   * - resHeader
     - string
     - 响应头（HTTP/Dubbo RPC/gRPC等）
     - 无
     - 必须，可为空
   * - resBody
     - string
     - 响应体（HTTP/Dubbo RPC/gRPC等）
     - 无
     - 必须，可为空
   * - clientIp
     - string
     - 客户端IP
     - 无
     - 必须
   * - language
     - string
     - Agent 对应的语言
     - 无
     - 必须
   * - replayRequest
     - boolean
     - 是否为重放请求
     - 无
     - 必须
   * - pool
     - []pool
     - 不可信参数的方法调用池数据
     - 无
     - 必须，可为空


pool 参数说明

.. list-table::
   :widths: 4 4 10 4 4
   :header-rows: 1
   :width: 100%
   
   * - 参数名
     - 类型
     - 描述
     - 默认值
     - 是否必须
   * - invokeId
     - int
     - 方法调用ID，单次HTTP请求中，确保唯一性
     - 无
     - 必须
   * - interfaces
     - array[string]
     - hook点处命中的类对应的接口及父类
     - 无
     - 必须，可为空
   * - targetHash
     - array[int]
     - 不可信数据经过该方法后，转换为的数据对应的hash值（确保唯一）
     - 无
     - 必须，可为空
   * - targetValues
     - string
     - 不可信数据经过该方法后，转换为的数据值
     - 无
     - 必须，可为空
   * - signature
     - string
     - 方法签名
     - 无
     - 必须
   * - originClassName
     - string
     - hook点处命中的类名称
     - 无
     - 必须
   * - vsourceValues
     - string
     - 不可信数据进入该方法时，对应的数据值
     - 无
     - 必须
   * - methodName
     - string
     - hook点处命中的方法名称
     - 无
     - 必须
   * - className
     - string
     - hook点处命中规则的类/接口名称
     - 无
     - 必须
   * - source
     - boolean
     - 是否为不可信数据来源方法
     - 无
     - 必须
   * - callerLineNumber
     - int
     - hook方法的调用行
     - 无
     - 必须
   * - callerClass
     - string
     - hook方法对应的调用方法所在的类名称
     - 无
     - 必须
   * - args
     - string
     - hook方法对应的方法参数值
     - 无
     - 必须，可为空
   * - callerMethod
     - string
     - hook方法的调用方法
     - 无
     - 必须
   * - sourceHash
     - array[int]
     - 不可信数据进入该方法时，数据对应的hash值（确保唯一）
     - 无
     - 必须
   * - retClassName
     - string
     - 返回值数据类型的类名
     - 无
     - 必须，可为空
