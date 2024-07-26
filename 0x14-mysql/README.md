# Setting up a MySQL master-slave replication 

Setting up a MySQL master-slave replication involves configuring one MySQL server to act as the master and another as the slave. The slave will replicate data changes from the master. Here’s a step-by-step guide to configuring MySQL master-slave replication:

### Prerequisites:
- Two MySQL servers (Master and Slave)
- MySQL installed on both servers
- Administrative access to both servers

### MySQL Master-Slave Replication Explained

Master-slave replication in MySQL involves a primary server (master) that receives updates and other servers (slaves) that replicate these changes. This setup enhances data redundancy, load balancing, and fault tolerance.

#### Key Concepts and Terms

1. **Master Server**: The primary server where data is written.
2. **Slave Server**: The secondary server(s) that replicate data from the master.
3. **Binary Logs**: Logs on the master that record all changes to the database.
4. **Relay Logs**: Logs on the slave that record changes retrieved from the master's binary logs.

### Detailed Steps and Options

#### 1. Configure the Master Server

**Step 1: Edit MySQL Configuration File**

- **Why**: The master server needs to be configured to log all changes made to the database. This is done using the binary log.
- **How**: Open the MySQL configuration file (`/etc/mysql/my.cnf`) and set the server ID and binary log options.

```ini
[mysqld]
server-id = 1
log_bin = /var/log/mysql/mysql-bin.log
binlog_do_db = your_database_name
```

- **Options**:
    - `server-id = 1`: Each server in a replication setup must have a unique server ID.
    - `log_bin`: Specifies the location of the binary log files.
    - `binlog_do_db`: Limits the logging to specific databases (optional).

**Step 2: Restart MySQL Service**

- **Why**: To apply the changes made to the MySQL configuration file.
- **How**: Use the following command to restart the MySQL service:

    ```bash
    sudo systemctl restart mysql
    ```

**Step 3: Create a Replication User**

- **Why**: A dedicated user is needed for the slave to authenticate and connect to the master.
- **How**: Execute the following SQL commands to create a replication user with the necessary permissions:

    ```sql
    CREATE USER 'replica_user'@'%' IDENTIFIED BY 'password';
    GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
    FLUSH PRIVILEGES;
    ```

    - `CREATE USER`: Creates a new user.
    - `GRANT REPLICATION SLAVE`: Grants the necessary permissions for replication.
    - `FLUSH PRIVILEGES`: Reloads the grant tables to ensure that the new privileges take effect.

**Step 4: Obtain Master Status Information**

- **Why**: You need to know the current position of the binary log so the slave can start replicating from that point.
- **How**: Execute the following commands:

    ```sql
    FLUSH TABLES WITH READ LOCK;
    SHOW MASTER STATUS;
    ```

    - `FLUSH TABLES WITH READ LOCK`: Prevents any new changes from being written to the tables, ensuring a consistent state.
    - `SHOW MASTER STATUS`: Displays the current binary log file and position.

    Note down the `File` and `Position` values from the output.

**Step 5: Export the Database**

- **Why**: To create a consistent snapshot of the database that can be imported into the slave.
- **How**: Use `mysqldump` to export the database:

    ```bash
    mysqldump -u root -p --databases your_database_name > db_backup.sql
    ```

#### 2. Configure the Slave Server

**Step 1: Edit MySQL Configuration File**

- **Why**: The slave server needs to be configured to receive and apply the changes from the master.
- **How**: Open the MySQL configuration file (`/etc/mysql/my.cnf`) and set the server ID and relay log options.

```ini
[mysqld]
server-id = 2
relay_log = /var/log/mysql/mysql-relay-bin.log
```

- **Options**:
    - `server-id = 2`: Unique identifier for the slave server.
    - `relay_log`: Specifies the location of the relay log files.

**Step 2: Restart MySQL Service**

- **Why**: To apply the changes made to the MySQL configuration file.
- **How**: Use the following command to restart the MySQL service:

    ```bash
    sudo systemctl restart mysql
    ```

**Step 3: Import the Database**

- **Why**: The slave needs to start with a consistent snapshot of the master’s data.
- **How**: Copy the database backup from the master to the slave and import it:

    ```bash
    scp user@master:/path/to/db_backup.sql /path/to/
    mysql -u root -p < /path/to/db_backup.sql
    ```

**Step 4: Configure Slave to Replicate from Master**

- **Why**: The slave needs to know where to connect to the master and from which log position to start replicating.
- **How**: Execute the following SQL commands:

    ```sql
    CHANGE MASTER TO
        MASTER_HOST='master_ip_address',
        MASTER_USER='replica_user',
        MASTER_PASSWORD='password',
        MASTER_LOG_FILE='mysql-bin.000001',
        MASTER_LOG_POS=12345;
    ```

    - `MASTER_HOST`: IP address or hostname of the master server.
    - `MASTER_USER`: Replication user created on the master.
    - `MASTER_PASSWORD`: Password for the replication user.
    - `MASTER_LOG_FILE`: Binary log file from `SHOW MASTER STATUS`.
    - `MASTER_LOG_POS`: Log position from `SHOW MASTER STATUS`.

**Step 5: Start the Slave**

- **Why**: To initiate the replication process on the slave.
- **How**: Execute the following SQL commands:

    ```sql
    START SLAVE;
    SHOW SLAVE STATUS\G
    ```

    - `START SLAVE`: Starts the replication process.
    - `SHOW SLAVE STATUS\G`: Displays detailed information about the slave’s replication status.

#### Monitoring and Maintenance

**Verify Replication Status**:

- **Why**: To ensure that replication is functioning correctly.
- **How**: Check the slave status:

    ```sql
    SHOW SLAVE STATUS\G
    ```

    - **Key Fields**:
        - `Slave_IO_Running`: Should be `Yes`.
        - `Slave_SQL_Running`: Should be `Yes`.
        - `Last_Error`: Should be empty or `None`.

**Restart Slave**:

- **Why**: If replication stops or encounters errors, you may need to restart it.
- **How**: Use the following SQL commands:

    ```sql
    STOP SLAVE;
    START SLAVE;
    ```

**Monitor Logs**:

- **Why**: To diagnose and troubleshoot replication issues.
- **How**: Check the MySQL error logs:

    ```bash
    tail -f /var/log/mysql/error.log
    ```

### Example Configuration Files

**Master: `/etc/mysql/my.cnf`**
```ini
[mysqld]
server-id = 1
log_bin = /var/log/mysql/mysql-bin.log
binlog_do_db = your_database_name
```

**Slave: `/etc/mysql/my.cnf`**
```ini
[mysqld]
server-id = 2
relay_log = /var/log/mysql/mysql-relay-bin.log
```

### Conclusion

Configuring MySQL master-slave replication involves setting up the master to log changes, creating a user for replication, and configuring the slave to replicate from the master. This setup enhances data availability and disaster recovery capabilities. Regular monitoring and maintenance are essential to ensure that replication continues to run smoothly and to address any issues that arise promptly.
