1. **Servers**:
   - Server 1: Hosts the Nginx web server.
   - Server 2: Hosts the application server and MySQL database.
   - Server 3: Acts as the load balancer (HAproxy).

2. **Web Server (Nginx)**:
   - Purpose: Handles HTTP requests, serves static content, and forwards dynamic requests to the application server.
   - Explanation: Nginx is a high-performance web server and reverse proxy known for its efficiency, scalability, and reliability. It serves as the entry point for user requests and optimizes the delivery of web content.

3. **Application Server**:
   - Purpose: Hosts the application logic, processes dynamic content, and interacts with the MySQL database.
   - Explanation: The application server executes the codebase of the website, generates dynamic content, and handles user interactions. It communicates with the database to retrieve and manipulate data required by the application.

4. **Load Balancer (HAproxy)**:
   - Purpose: Distributes incoming HTTP requests across multiple web servers to improve performance, scalability, and reliability.
   - Explanation: The load balancer ensures that incoming traffic is evenly distributed among the available web servers, preventing any single server from becoming overwhelmed. It enhances the availability and fault tolerance of the web infrastructure.

5. **Application Files (Code Base)**:
   - Purpose: Contains the source code of the website, including HTML, CSS, JavaScript, server-side scripts, and other assets.
   - Explanation: The application files define the functionality and behavior of the website. They are deployed on the application server and executed to generate dynamic content for the web pages.

6. **Database (MySQL)**:
   - Purpose: Stores and manages the website's data, including user information, content, and session data.
   - Explanation: MySQL is a relational database management system (RDBMS) known for its reliability, scalability, and performance. It provides persistent storage for the application data and supports features such as transactions, indexing, and querying.

**Load Balancer Configuration**:
- The load balancer (HAproxy) is configured with a round-robin distribution algorithm. This algorithm evenly distributes incoming HTTP requests among the available web servers in a circular manner.

**Active-Active vs. Active-Passive Setup**:
- The load balancer enables an Active-Active setup, where both web servers are actively serving requests simultaneously.
- In an Active-Active setup, both servers are fully functional and actively handling incoming traffic, providing redundancy and load distribution.
- In contrast, an Active-Passive setup would involve one server actively serving traffic while the other server remains in standby mode, ready to take over in case of a failure or overload on the active server.

**Primary-Replica (Master-Slave) Database Cluster**:
- The MySQL database is configured as a Primary-Replica (Master-Slave) cluster.
- In this setup, the Primary node (Master) handles write operations and serves as the authoritative source of data.
- Replica nodes (Slaves) replicate data from the Primary node for read-only access, providing redundancy and scalability.
- The Primary node is responsible for processing write operations and maintaining data consistency, while Replica nodes serve read-only requests to offload the Primary node and improve read performance.

**Issues with the Infrastructure**:

1. **Single Point of Failure (SPOF)**:
   - The infrastructure may still have single points of failure, such as the load balancer or database server, which could lead to downtime or service interruptions if they fail.

2. **Security Issues**:
   - The infrastructure lacks security measures such as firewalls and HTTPS encryption, making it vulnerable to unauthorized access, data breaches, and interception of sensitive information.

3. **No Monitoring**:
   - Without monitoring tools in place, it is challenging to detect and address performance issues, security threats, or infrastructure failures proactively. Lack of monitoring can lead to prolonged downtime, degraded performance, and compromised security.
