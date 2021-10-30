Deployment Guides
===================
Docker Compose
-------------------
Requirements
+++++++++++++++++
- Docker
- docker-compose

.. tip:: Which can be checked by running ``docker -v`` and ``docker-compose``.

Setup
+++++++++

.. tabs:: **Deploy**

   .. code-block:: bash

      # Clone the repository
      git clone https://github.com/HXSecurity/DongTai.git
      cd deploy/docker-compose/

      # Deploy
      ./install.sh
      
.. tip:: **Custom Configuration**

  Open :blue:`config-tutorial.ini` to configure ``mysql`` and ``redis`` and then refer to :doc:`initial configuration custom database <../03_config/01_server>` if you want to use your own database.

  After that use ``-s`` to skip the relevant component in your deployment step as following:
  
  .. code-block:: bash

     ./install.sh  -s mysql

  - s: skip specified component, optional: ``mysql`` ``redis`` ``mysql,redis``, default: don't skip
  

Kubernetes
---------------
Requirements
+++++++++++++++

- Kubernetes version: 1.9+

- Kubectl has been installed on the client

- You can use ``kubectl auth can-i`` if you have authorization for the following operations：

  - create secrets

  - create deployments

  - create configmaps

  - create namespaces

  - create StatefulSet

  - create Service


Setup via Script
+++++++++++++++++++
.. tabs:: **Deploy**

   .. code-block:: bash

      # Clone the repository
      git clone https://github.com/HXSecurity/DongTai.git
      cd deploy/kubernetes

      # Deploy
      ./install.sh -m NodePort -n dongtai

.. tabs:: **Undeploy**

      .. code-block:: bash
            
         kubectl delete namespace ${YourNamespace}

.. tip:: **Custom Configuration**

    - m: access mode(mode), optional: ``NodePort`` ``LoadBalancer``, default: NodePort

    - s: skipped resources(skip), optional: ``mysql`` ``redis`` ``mysql,redis``, default: don't skip

    - n: specify the namespace, default: ``dongtai``

    
    Navigate to :blue:`manifest/4.deploy-iast-server.yml` to configure ``[mysql]`` and ``[redis]`` and then refer to :doc:`initial configuration custom database <../03_config/01_server>` if you want to use your own database.

    **Access**

    - NodePort
      
      - Obtain an available Node IP address

        .. code-block:: bash

           kubectl get nodes -o wide |  awk {'print $1" " $2 " " $7'} | column -t

      - Obtain an available NodePort

        .. code-block:: bash

            kubectl get svc dongtai-web-pub-svc -n dongtai-iast -o=jsonpath='{.spec.ports[0].nodePort}'
            kubectl get svc dongtai-engine-pub-svc -n dongtai-iast -o=jsonpath='{.spec.ports[0].nodePort}')

      - Access Link:
      
        .. code-block:: bash

            http://${NodeIP}:${PORT}

    - LoadBalancer

      - Obtain the available LoadBalancer IP address or DNS

        .. code-block:: bash

           kubectl get svc dongtai-web-pub-svc dongtai-engine-pub-svc -n dongtai-iast



Setup via Helm
+++++++++++++++++++

*Before installation, ensure helm is available. Follow the instruction to install* |helm|.

.. |helm| raw:: html

   <a href="https://helm.sh/docs/intro/install/" target="_blank">helm</a>


.. tabs:: **Deploy**

   .. code-block:: bash

      # Clone the repository
      git clone https://github.com/HXSecurity/DongTai.git
      cd deploy/kubernetes/helm

      # Add and update helm chart repo for Dongtai IAST
      helm repo add dongtai https://charts.dongtai.io/iast
      helm repo update

      # Deploy
      helm install --create-namespace -n dongtai  dongtai-iast dongtai/dongtai-iast

This command will deploy DongTai IAST Server in ``dongtai`` namespace and expose service with ``ClusterIP``.

.. tabs:: **Undeploy**

      .. code-block:: bash
            
         helm uninstall dongtai-iast -n dongtai


.. tip:: **Custom Configuration**

  - Navigate to :blue:`/tmp/my-values.yml` to modify ``mysql`` and ``redis`` and then refer to :doc:`initial configuration custom database <../03_config/01_server>` if you want to use your own database.
     
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

  - Or you can pass in a single value using ``--set``. For example, you can switch the default access type ``ClusterIP`` to ``NodePort`` by the following command:

    .. code-block:: bash

       helm install --create-namespace -n dongtai-test --set accessType=NodePort dongtai-iast dongtai/dongtai-iast
  
    Avaliable values:

    - skipMysql: false (default), skipRedis: false (default)

    - accessType: ClusterIP(default), Options: ``ClusterIP``, ``NodePort``, ``LoadBalancer``

    - imageVersion: latest (default)
  

After Deployment
-----------------
.. important:: 
  
  After the deployment, access it with your specified ``web service port``, e.g.: localhost

  - Default account and password: admin/admin; 
    
  - You :red:`MUST` change the password during the first time log in. 
    
    Password can be changed at :blue:`Settings > Account`.  After that, you can log in again.
  
  - Navigating to :blue:`Settings > Service Registration` to set up the ``DongTai-OpenAPI`` URL first after log in to the platform.

.. seealso:: 
  
  We also provide DongTai IAST Sever SaaS version. For detail refer to :doc:`register <../04_ops/00_register>`.
    