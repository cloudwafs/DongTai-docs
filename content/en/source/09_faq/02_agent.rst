Agent
=================
Installation
------------------------

- **If multiple projects share one Agent, how will the vulnerability information collected in the background be displayed?**

  - When multiple projects share one Agent, all vulnerability data can be viewed on the ``Application Vulnerability`` page.
  
  - If you need to distinguish between different projects, you can add the startup parameter of the project ``-Dproject.name=project name``, and then create a new project, the project name and the parameter ``-Dproject.name=project name`` in the the project name is the same, and the vulnerability information will be displayed in the created project.

- **How ​​to get Token?**

  :doc:`Please refer to Dongtai IAST Proxy Plugin Guide <../05_ext/01_plugin>`> Configure Plugin> Get ``Token``

- **Can multiple app.jar share the same agent.jar?**
 
  Yes, if you need to distinguish between different projects, you can specify the startup parameter ``project.name``

- **What should I do if an error message appears after starting the project with Agent?**

  Without affecting the use of the project, the Agent will have a chance to report an error during detection. This is a normal phenomenon.

  Otherwise, please save the error log and contact the technical staff

- **How ​​to update the probe?**

  :blue:`System Configuration> Status Monitoring`, click :blue:`Cloud Probe Service` on the upper right corner to refresh

- **Does the project name need to be unique?**

  For projects under the same user, each project name :red:`must` is unique

- **Agent has been changed after re-downloading, but the project name is still the same. Is it possible to verify the vulnerability?**

  - Need to be the same Agent

- **Why is the probe not detected from the DongTai IAST Server after starting the project?**

  :doc:`Please refer to the Agent Installation Guide <../02_start/03_agent>`> Troubleshooting

- **How ​​to bind multiple versions of the project? What about the vulnerability data display?**
  
  - When creating a new project on the Dongtai IAST official website, there is an input box to fill in the version, and fill in the current application version. When the application is updated with a new version, first enter the details of the previously built project. You can edit the version at ``Version``, add a new version and switch to the new version, and then start the new version application.
  
  - The vulnerability data of different versions will be displayed in the corresponding version of the project.

- ** Which Java version does the Java Agent support?**

  :doc:`Please refer to the Agent Installation Guide Guide <../02_start/03_agent>`> Java Agent> Installation Environment

- **The system configuration is normal and the number of requests is normal, why no loopholes are displayed?**

  - The system is delayed, wait a few minutes before refreshing

Vulnerability Detection
------------------------------

- **Does the rule method support regularization?**
  
  - The hook method does not support regularization for the time being
  - It is recommended to use the IDEA plugin to add rules

- **If you add a custom rule, how the rule is related to the vulnerability information and the taint flow graph**

  Used XSS rules as an example:

  - If it is to filter xss, add it to the filter method

  - If it is the vulnerability trigger point of xss, add it to the dangerous method

- **What is the difference between the filtering method rule and the dangerous method rule in the vulnerability detection mechanism?**

  - The filtering method rule is a kind of propagation node, which is used to add the company's internal customized dangerous data filtering method
  
  - The dangerous method is where the vulnerability starts

- **Does the DongTai IAST Server support proxy during scanning? If the business service interface cannot be accessed normally, but the reverse direction is OK, can it still be detected normally?**

  DongTai IAST does not have a scanning function, so there is no need to initiate a request to the business server

- **The detection of component management vulnerability is for all jar packages on the host where the Agent is located?**

  Only detect packages that the application depends on

- **Is the purpose of the verification function to verify whether the vulnerability exists?**

  Yes, in order to verify whether the vulnerability exists

- **Dirty data may be generated when sending a verification request?**

  There will be no dirty data, the replay request has a replay mark, and it will be automatically intercepted

- **When performing verification, will the integrated PoC verification be automatically invoked according to the type?**

  For the time being, the type is not distinguished, and the unified PoC ``./../\`/dongtai`` is directly called for verification, and the custom PoC will be supported later

- **Will the DongTai IAST determine that the polluted data is offensive?**

  Not temporarily

- **Where can I look at the taint parameter tracking chart?**

  Built-in search function, search the url or related information of the vulnerability to display the taint parameter tracking graph