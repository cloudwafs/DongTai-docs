Server 部署指南
===================
Docker Compose
-------------------
系统需求
+++++++++++++++++
- Docker
- docker-compose

.. tip:: 
  
  可通过运行 ``docker -v`` 和 ``docker-compose`` 来检查查看当前机器是否已经安装。

部署设置
+++++++++

.. tabs:: **部署**

   .. code-block:: bash

      # 克隆存储库
      git clone https://github.com/HXSecurity/DongTai.git
      cd deploy/docker-compose/

      # 部署
      ./install.sh
      
.. tip:: **自定义配置**

  使用自定义数据库，请手动修改 :blue:`config-tutorial.ini` 文件内的 ``mysql`` 和 ``redis`` 配置后再参照 :doc:`初始化自定义数据库 <../03_config/01_server>`。

  修改完成后,在下述的部署过程选择 ``-s`` 略过相应的组件:
  
  .. code-block:: bash

     ./install.sh  -s mysql

  - s: 跳过的资源(skip), 可选: ``mysql`` ``redis`` ``mysql,redis``, 默认：不跳过
  

Kubernetes
---------------
系统需求
+++++++++++++++

- Kubernetes version: 1.9+

- 客户端已经安装 Kubectl

- 具备以下操作的授权,可以使用 ``kubectl auth can-i`` 验证:

  - create secrets

  - create deployments

  - create configmaps

  - create namespaces

  - create StatefulSet

  - create Service


脚本部署
+++++++++++++++++++
.. tabs:: **部署**

   .. code-block:: bash

      # 克隆存储库
      git clone https://github.com/HXSecurity/DongTai.git
      cd deploy/kubernetes

      # 部署
      ./install.sh -m NodePort -n dongtai

.. tabs:: **卸载**

      .. code-block:: bash
            
         kubectl delete namespace ${YourNamespace}

.. tip:: **自定义配置**

    - m: 访问模式(mode)，可选: ``NodePort`` ``LoadBalancer``, 默认为: NodePort

    - s: 跳过的资源(skip), 可选: ``mysql`` ``redis`` ``mysql,redis``, 默认: don't skip

    - n: 指定 namespace, 默认: ``dongtai``

    
    使用自定义数据库，手动修改 :blue:`manifest/4.deploy-iast-server.yml` 文件内的 ``mysql`` 和 ``redis`` 配置后再参照 :doc:`初始化自定义数据库 <../03_config/01_server>`。

    **访问**

    - NodePort
      
      - 获取可用的 NodePort

        .. code-block:: bash

           kubectl get nodes -o wide |  awk {'print $1" " $2 " " $7'} | column -t

      - 获取可用的 NodePort

        .. code-block:: bash

            kubectl get svc dongtai-web-pub-svc -n dongtai-iast -o=jsonpath='{.spec.ports[0].nodePort}'
            kubectl get svc dongtai-engine-pub-svc -n dongtai-iast -o=jsonpath='{.spec.ports[0].nodePort}')

      - 访问地址:
      
        .. code-block:: bash

            http://${NodeIP}:${PORT}

    - LoadBalancer

      - 获取可用的 LoadBalancer IP 或者 DNS

        .. code-block:: bash

           kubectl get svc dongtai-web-pub-svc dongtai-engine-pub-svc -n dongtai-iast



Helm 部署
+++++++++++++++++++

*安装之前请确保已经安装 Helm。安装指南：* |helm|.

.. |helm| raw:: html

   <a href="https://helm.sh/docs/intro/install/" target="_blank">helm</a>


.. tabs:: **部署**

   .. code-block:: bash

      # 克隆存储库
      git clone https://github.com/HXSecurity/DongTai.git
      cd deploy/kubernetes/helm

      # 添加、更新仓库
      helm repo add dongtai https://charts.dongtai.io/iast
      helm repo update

      # 部署
      helm install --create-namespace -n dongtai  dongtai-iast dongtai/dongtai-iast

这个命令将会在 ``dongtai`` 命名空间部署 Dongtai IAST Server , 并且使用 ``ClusterIP`` 方式暴露服务.

.. tabs:: **卸载**

      .. code-block:: bash
            
         helm uninstall dongtai-iast -n dongtai


.. tip:: **自定义配置**

  - 使用自定义数据库，手动修改 :blue:`/tmp/my-values.yml` 文件内的 ``mysql`` 和 ``redis`` 配置后再参照 :doc:`初始化自定义数据库 <../03_config/01_server>`。
     
    .. code-block:: yaml
        
        mysql:
          host: my-dongtai-mysql
          port: 3306
          name: my-dongtai_webapi
          user: root
          password: my-dongtai-iast

        redis:
          host: my-dongtai-redis
          port: 6379
          password: 123456
          db: 0

    .. code-block:: bash

       helm install --create-namespace -n dongtai --values /tmp/my-values.yaml dongtai-iast dongtai/dongtai-iast

  - 你也可以使用 ``--set`` 来覆盖单个值, 你可以使用 ``--set`` 将 ``ClusterIP`` 切换成 ``NodePort``:

    .. code-block:: bash

       helm install --create-namespace -n dongtai-test --set accessType=NodePort dongtai-iast dongtai/dongtai-iast
  
    Avaliable values:

    - skipMysql: false (默认值), skipRedis: false (默认值)

    - accessType: ClusterIP(默认值), 可选项: ``ClusterIP``, ``NodePort``, ``LoadBalancer``

    - imageVersion: latest (默认值)
  

部署后
-----------------
.. important:: 
  
  环境启动成功后，通过部署过程中指定的 ``web service port`` 访问即可。

  - 默认账号及密码: admin/admin; 
    
  - 首次登入 :red:`必须` 修改密码。
  
    至 :blue:`系统配置 > 密码修改` 修改密码后再重新登入。
  
  - 首次登入也请在 :blue:`系统配置 > 服务注册` 中配置 ``DongTai-OpenAPI``。

.. seealso:: 
  
  我们也提供 ``DongTai IAST Server 端 SaaS 版本``。请至此链接 :doc:`注册账户 <../04_ops/00_register>`。
    