Agent Installation Guides
===========================
Downloading Agent
----------------------
#. Login to DongTai IAST Server and navigate to :blue:`Add Agent` which locate at the upper-right of the site.

#. Select a language and dowload the agent.

.. image:: ../_static/02_start/dl-agent.png
  :alt: downloading agent

Java Agent
--------------
Requirements
++++++++++++++++
- Check whether the service of installing the probe and the OPENAPI service are network interoperable.

- Ensure the service of installing DongTai Agent meet the requirement as below:

  - Operating system: Windows/Linux/Unix

  - JDK version: 1.6 and above

  - Framework: Any

  - Middleware: Any

Install via Command Line
++++++++++++++++++++++++++++++++

.. code-block::

   java -jar agent.jar -m install -p <pid>

Install via Configure
+++++++++++++++++++++++++++++++++++++++++++

.. tabs::

   .. tab:: **SpringBoot**
       
       #. Move the ``agent.jar`` to the directory which allows read and write permission, such: :blue:`/tmp/`.
       
       #. For Spring Boot application 
       
          a. If the application is deployed by WAR, attach the agent to it by following the middleware you use. 
          
          b. If the application is deployed by JAR. Add the following arguments: 
          
          .. code-block:: bash
              
              java -javaagent:/path/to/agent.jar -jar <app>.jar

   .. tab:: **Tomcat**
       
       Navigate to Tomcat's bin directory and open the :blue:`/catalina.sh` file in text editor. Add the following settings at the first line of text:
       
       .. code-block:: bash
           
           CATALINA_OPTS="-javaagent:/path/to/server/agent.jar -Dproject.name=<application name>"

   .. tab:: **Jetty**
       
       Add the following arguments:
       
       .. code-block:: bash
           
           java -javaagent:/path/to/agent.jar -Dproject.name=<project name> -jar <app>.jar
                 
   .. tab:: **JBoss**
       
       **JBoss AS 6**
       
       - Navigate to JBoss's bin directory and open the :blue:`/run.sh` file in text editor. 
         Find :blue:`# Setup JBoss specific properties` in the text and add the following line below it:

       .. code-block:: bash

           JAVA_OPTS="$JAVA_OPTS "-javaagent:/path/to/agent.jar" "-Dproject.name=<application name>
           
       **JBoss AS 7、JBoss Wildfly**

       - Navigate to JBoss's bin directory and modify the setting's value according to the server mode: ``standalone mode`` or ``domain mode``.
       
         - Standalone Mode
         
           Open :blue:`/standalone.sh` file in the text editor and find :blue:`# Display our environment` in the text. 
         
           Add the following line above it:

         .. code-block:: bash
             
             JAVA_OPTS="$JAVA_OPTS "-javaagent:/path/to/agent.jar" "-Dproject.name=<application name>


         - Domain Mode
            - Settings of Server Group

            .. code-block:: bash
            
                <jvm-options>
                    <option value="-javaagent:<jboss_root>/path/to/agent.jar"/>
                    <option value="-Dproject.name=<project name>"/>
                </jvm-options>

            - Settings of Server

            .. code-block:: bash
                
                <jvm name="default">
                    <jvm-options>
                        <option value="-javaagent:<jboss_root>/rasp/rasp.jar"/>
                        <option value="-Dproject.name=<project name>"/>
                    </jvm-options>
                </jvm>
           
   .. tab:: **Resin**
        
        Navigate to Resin's conf directory and open :blue:`/cluster-default.xml` file with text editor. 
        Find :blue:`server-default` in the text and add the following line below it:

        .. code-block:: bash
            
            <jvm-arg>-javaagent:/opt/agent/agent.jar</jvm-arg> <jvm-arg>-Dproject.name=<application name></jvm-arg>

   .. tab:: **WebLogic**
       
       **Via WebLogic Server Administration Console**
       
       #. Navigate to :blue:`Domain Structure > Environment > Servers` and select the application server which is going to install the agent from the table.
       
       #. Navigate to :blue:`Server Start` in :blue:`Summary of Servers` and add the following line into :blue:`Arguments`.
       
       .. code-block:: bash
           
            JAVA_OPTS="$JAVA_OPTS "-javaagent:/path/to/agent.jar" "-Dproject.name=<application name> 

       #. Restart service to apply the new settings

       **Via edit config.xml in WebLogic**

       #. Navigate to the following WebLogis's directory :blue:`/u01/oracle/weblogic/user_projects/domains/base_domain/config` and open :blue:`config.xml` file with text editor.
       
       #. Find the sub-element of :blue:`<server-start>` which is :blue:`<arguments>`, then add the following content into the sub-element:

       .. code-block:: bash

            -javaagent:/path/to/agent.jar -Dproject.name=<application name>

   .. tab:: **WebSphere**

       #. From WebSphere Admin Console, navigate to :blue:`Server > Server Types > WebSphere Application Server`.

       #. Select the application server which is going the agent and navigate to :blue:`Server Infrastructure > Process definition`.

       #. Then head to :blue:`Additional Properties > Java Virtual Machine`.

       #. Find the :blue:`Generic JVM arguments`, then add the following line and save the change.

       .. code-block:: bash

            -javaagent:/path/to/agent.jar -Dproject.name=<application name>
.. tip:: 
       
    Keep the ``<application name>`` consistent with the ``application name`` that has created, otherwise `Demo Project` will be default. 

    The agent can associate the application automatically with adding ``-Dproject.create=true``.

    You also can manually associate it in application settings at the DongTai IAST Server to keep the parameters value blank.

Python Agent
----------------
Requirements
++++++++++++++++
- Check whether the service of installing the probe and the OPENAPI service are network interoperable.

- Ensure the service of installing DongTai Agent meet the requirement as below:

  - Operating system: Windows/Linux/Unix

  - Python version：3.3 and above

  - Interpreter：CPython

  - Middleware：uWSGI

  - Web Framework：Django

  - Web Service：Django REST Framework

  - Python Dependencies：psutil >= 5.8.0，requests >= 2.25.1，pip >= 19.2.3

Install Agent
+++++++++++++++++++++++++++++++++

.. code-block::

   pip3 install ./dongtai-agent-python.tar.gz

Configure Agent
+++++++++++++++++++++++++++++++++++++++++++
.. tabs::

   .. tab:: **Django**
       
       1. Navigate to Django application directories which is going to install the agent.
       
       2. Modify the settings.py file and find MIDDLEWARE in the file.
       
       3. Add the following line:

       .. code-block:: python

           MIDDLEWARE = [ 
               'dongtai_agent_python.middlewares.django_middleware.FireMiddleware',
               #...
            ]  

   .. tab:: **Flask**
         
       1. Modify the <app.py> file and add the following line:

       .. code-block:: python
           
           app = Flask(__name__)
           
           # Add agent
           from dongtai_agent_python.middlewares.flask_middleware import AgentMiddleware
           app.wsgi_app = AgentMiddleware(app.wsgi_app, app)
           

Restart Service
+++++++++++++++++++++++++++++++++++++++++++

Use ``dongtai-cli run <arguments>`` to start the application. 

Example:

.. code-block:: bash
    
    # Django
    $ dongtai-cli run python manage.py runserver ...
    # or
    # Flask
    $ dongtai-cli run flask run ...
    # or
    $ dongtai-cli run uwsgi ... 

.. tip:: 
       
    Keep the ``<application name>`` consistent with the ``application name`` that has created, otherwise `Demo Project` will be default. 

    The agent can associate the application automatically with adding ``-Dproject.create=true``.

    You also can manually associate it in application settings at the DongTai IAST Server to keep the parameters value blank.

Troubleshooting
-------------------
.. note::

    Start/Restart the Web Service and then access it with the browser.
    
    Once registered, the agent should appear in the DongTai IAST Server :blue:`Settings > Agent` list.
    
    If you do not see the agent on list within a few minutes, check the following:

    1. Check the agent.jar
    
      Execute the following command ``java -jar /temp/agent.jar`` to check it is working. 
      
      Please re-download the agent file and try again otherwise. 
      
      If the problem still persists, you can directly report the issue to us on |GitHub| and we will get you an answer back shortly.

    2. Check the network connection

      If the Web Service is unable to access to https://openapi.iast.io.
      
      Please check the network connection and try again. 
      
      Otherwise, you can directly report the issue to us on |GitHub| and we will get you an answer back shortly.


.. |GitHub| raw:: html

   <a href="https://github.com/HXSecurity/DongTai/discussions" target="_blank">GitHub</a>

    
