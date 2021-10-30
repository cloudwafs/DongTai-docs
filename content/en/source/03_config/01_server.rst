Server Initial and Upgrade
===============================

Initial Configuration Custom Database
--------------------------------------------
.. code-block:: bash
    
    # Download database scheme
    wget https://huoqi-public.oss-cn-beijing.aliyuncs.com/iast/sql/db.sql
    wget https://huoqi-public.oss-cn-beijing.aliyuncs.com/iast/sql/rule.sql
    wget https://huoqi-public.oss-cn-beijing.aliyuncs.com/iast/sql/sca.sql
    wget https://huoqi-public.oss-cn-beijing.aliyuncs.com/iast/sql/update-20210401.sql
    wget https://huoqi-public.oss-cn-beijing.aliyuncs.com/iast/sql/update-20210702.sql
    wget https://huoqi-public.oss-cn-beijing.aliyuncs.com/iast/sql/update-20210717.sql
    wget https://huoqi-public.oss-cn-beijing.aliyuncs.com/iast/sql/update-20210731.sql
    wget https://huoqi-public.oss-cn-beijing.aliyuncs.com/iast/sql/update-20210817.sql
    wget https://huoqi-public.oss-cn-beijing.aliyuncs.com/iast/sql/update-20210831.sql
    wget https://huoqi-public.oss-cn-beijing.aliyuncs.com/iast/sql/update-20210918.sql
    wget https://huoqi-public.oss-cn-beijing.aliyuncs.com/iast/sql/update-20211009.sql
    wget https://huoqi-public.oss-cn-beijing.aliyuncs.com/iast/sql/update-20211022.sql
    
    # Executing the SQL file above by order via MySQL command to upgrade the database.
    mysql -u root -p <passwor> -D <database> < /docker-entrypoint-initdb.d/db.sql
    mysql -u root -p <passwor> -D <database> < /docker-entrypoint-initdb.d/rule.sql
    mysql -u root -p <passwor> -D <database> < /docker-entrypoint-initdb.d/sca.sql
    mysql -u root -p <passwor> -D <database> < /docker-entrypoint-initdb.d/update-*.sql


Upgrade DongTai IAST Server 
------------------------------------------
Step 1: Update installation package to latest version
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: bash

    # Change to DongTai directory, e.g.：/opt/DongTai
    git stash
    git pull
    git checkout release-<latest version>

Step 2: Run script to start deployment process
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: bash

    # Stop all DongTai IAST services in docker
    docker stop dongtai-iast_dongtai-engine-task_1 dongtai-iast_dongtai-web_1 dongtai-iast_dongtai-engine_1 dongtai-iast_dongtai-webapi_1 dongtai-iast_dongtai-openapi_1 dongtai-iast_dongtai-redis_1 dongtai-iast_dongtai-mysql_1

    cd deploy/docker-compose
    chmod u+x install.sh
    ./install.sh

Step 3: Update Database
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. attention::

    If you are not using the previous version, please :red:`UPDATE` you database SQL update file to the previous version before execute the following step.

- Entering ``dongtai-mysql`` container:

  .. code-block:: bash

      docker exec -it dongtai-iast_dongtai-mysql_1 /bin/bash

- Navigating to :blue:`/docker-entrypoint-initdb.d`, and then download the SQL update file: :blue:`update-20211022.sql`

  .. code-block:: bash

      cd /docker-entrypoint-initdb.d
      mysql -uroot -p"dongtai-iast" -D dongtai_webapi < /docker-entrypoint-initdb.d/update-20211022.sql

