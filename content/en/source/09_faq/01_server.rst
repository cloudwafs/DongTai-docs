Server
==========
Deployment
-------------------------

- **Does the server support docker deployment?**

  Support, :doc:`Please refer to the deployment guide <../02_start/02_deploy>`

- **How ​​to initialize the database when using a local database?**

  :doc:`Please refer to the deployment guide <../03_config/01_server>`

- **The reason for the failure to pull the image or the code during deployment?**

  -Pull the image: check if the network can access Docker Hub

  -Pull code: Check whether the network can access GitHub

- **Does the local installation have any requirements for server resources?**

  It is recommended that at least 4 Core 8 GB, :doc:`Please refer to the deployment guide <../02_start/02_deploy>` for the system requirements of each deployment method

- **Where can you get dongtai-openapi?**

  .. code-block:: bash
      
      #Execute instructions
      sudo docker ps -a | grep dongtai-iast_dongtai-openapi_1
      
      #Result, port is 8000
      #4d12c7952f5d dongtai/dongtai-openapi:1.0.6 "/usr/local/bin/uwsg…" 7 days ago Up 7 days 0.0.0.0:8000->8000/tcp, :::8000->8000/tcp dongtai- iast_dongtai-openapi_1

- **How ​​to deploy multiple openAPI service nodes? (Based on docker-compose method)**

  Create a few more openapi services, map the ports, hang up nginx in front, and configure load balancing

- **Database verification code cannot be displayed?**

  .. code-block:: bash

      #Remove from build_with_docker_compose.sh:
      volumes:
      ./data:/var/lib/mysql
      
      #implement
      run build_with_docker_compose.sh

- **Centos7 deployment report chown mod /var/lib/mysql permission denied, how to solve it?**

  - ``getenforce`` to see if ``selinux`` is enabled

  - If enabled, use ``setenforce 0``, disable ``getenforce``

  - If it still doesn't work, add ``--`` to the container that needs to map the file