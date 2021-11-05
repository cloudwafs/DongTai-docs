Server
==========
部署相关
---------

- **服务端是否支持docker部署？**

  支持，:doc:`请参考部署指南 <../02_start/02_deploy>`

- **使用本地数据库时，如何初始化数据库？**

  :doc:`请参考部署指南 <../03_config/01_server>`

- **部署时拉取镜像或者代码失败的原因？**

  - 检查网络是否能访问阿里云

  - 检查网络是否能访问 github

- **本地安装对服务器资源有什么要求吗？**

  建议至少 4 Core 8 GB, :doc:`请参考部署指南 <../02_start/02_deploy>` 中各部署方式之系统需求

- **dongtai-openapi 从哪里获取？**

  .. code-block:: bash
      
      #执行指令
      sudo docker ps -a | grep dongtai-iast_dongtai-openapi_1
      
      #结果，port 为 8000
      #4d12c7952f5d   dongtai/dongtai-openapi:1.0.6   "/usr/local/bin/uwsg…"   7 days ago   Up 7 days               0.0.0.0:8000->8000/tcp, :::8000->8000/tcp            dongtai-iast_dongtai-openapi_1

- **如何部署多个openAPI服务节点？(基于docker-compose方式)**

  - 多起几个 openapi 服务，端口映射出来，前面挂一下 nginx，配置负载均衡

- **数据库验证码无法显示?**

  .. code-block:: bash

      #从 build_with_docker_compose.sh 中移除：
      volumes:
      ./data:/var/lib/mysql
      
      #执行
      run build_with_docker_compose.sh

- **Centos7部署报chown mod /var/lib/mysql permission denied，如何解决?**

  - ``getenforce`` 查看 ``selinux`` 是否开启

  - 若开启使用 ``setenforce 0`` 关闭 ``getenforce``

  - 仍不行就给需要映射文件的容器加上 ``--``






