# Secured_and_monitored_web_infrastructure

1**Servers**:
   - Server 1: Hosts the Nginx web server and serves as the load balancer.
   - Server 2: Hosts the application server.
   - Server 3: Hosts the MySQL database.

2. **Firewalls**:
   - Purpose: Firewalls are added to control and monitor incoming and outgoing network traffic, providing security by filtering based on predefined rules.
   - Explanation: Firewalls help protect the infrastructure from unauthorized access, malicious attacks, and potential security breaches by enforcing security policies and preventing unauthorized access to sensitive resources.

3. **SSL Certificate for HTTPS**:
   - Purpose: An SSL certificate is added to encrypt data transmitted between the user's browser and the web server, ensuring data confidentiality and integrity.
   - Explanation: Serving traffic over HTTPS protects sensitive information such as login credentials, personal data, and financial transactions from eavesdropping and interception by unauthorized parties.

4. **Monitoring Clients (Data Collectors)**:
   - Purpose: Monitoring clients are installed on the servers to collect and send metrics, logs, and performance data to a centralized monitoring service such as Sumo Logic or other monitoring tools.
   - Explanation: Monitoring is essential for proactively identifying and addressing issues, optimizing performance, and ensuring the availability and reliability of the infrastructure and services.

**Firewalls**:
- Firewalls are added to control and monitor network traffic, enforce security policies, and protect the infrastructure from unauthorized access, threats, and attacks.

**SSL/TLS Encryption (HTTPS)**:
- Traffic is served over HTTPS to ensure secure communication between clients and the web server. HTTPS encrypts data transmitted over the network using SSL/TLS protocols, providing confidentiality and integrity.

**Monitoring Purpose**:
- Monitoring is used to track the performance, health, and availability of the infrastructure, applications, and services in real-time.
- It helps identify and diagnose issues, optimize resource usage, and ensure the reliability and scalability of the environment.

**Monitoring Data Collection**:
- The monitoring tool collects data from monitoring clients installed on the servers by gathering metrics, logs, events, and performance data.
- Monitoring clients periodically send data to the monitoring tool, which aggregates, analyzes, and visualizes the data to provide insights into the health and performance of the infrastructure.

**Monitoring Web Server QPS (Queries Per Second)**:
- To monitor the web server's QPS, you would configure the monitoring tool to collect and analyze relevant metrics related to incoming requests, such as HTTP request count, response time, and error rate.
- Additionally, you can set up dashboards and alerts to monitor QPS trends, identify spikes or drops in traffic, and proactively address any performance issues or bottlenecks on the web server.

**Issues with the Infrastructure**:

1. **Terminating SSL at the Load Balancer Level**:
   - Terminating SSL at the load balancer level can be an issue because it adds an additional point of vulnerability. If the load balancer is compromised, attackers can intercept decrypted traffic before it reaches the web server.

2. **Single MySQL Server Capable of Accepting Writes**:
   - Having only one MySQL server capable of accepting writes creates a single point of failure. If the MySQL server goes down, the website's functionality could be severely impacted, leading to downtime and data loss.

3. **Identical Server Components**:
   - Having servers with all the same components (database, web server, and application server) might be a problem because it increases the risk of a widespread failure. If there is a flaw or issue in one component, it could affect all servers, leading to widespread downtime and service interruptions.
