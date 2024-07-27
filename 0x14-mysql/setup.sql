-- Create the user 'holberton_user' if it does not exist, with password 'projectcorrection280hbtn'
CREATE USER IF NOT EXISTS holberton_user@localhost IDENTIFIED BY 'projectcorrection280hbtn';

-- Create the user 'replica_user' if it does not exist, with password '#replica_user@012', accessible from any host
CREATE USER IF NOT EXISTS replica_user@'%' IDENTIFIED BY "#replica_user@012";

-- Create the database 'tyrell_corp' if it does not exist
CREATE DATABASE IF NOT EXISTS tyrell_corp;

-- Select the database 'tyrell_corp' to use for subsequent commands
USE tyrell_corp;

-- Create the table 'nexus6' if it does not exist, with columns 'id' (auto-incrementing primary key) and 'name'
CREATE TABLE IF NOT EXISTS nexus6 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);

-- Insert a row into the 'nexus6' table with the value 'Martha' for the 'name' column
INSERT INTO nexus6 (name) VALUES ('Martha');

-- Grant the 'REPLICATION CLIENT' privilege to 'holberton_user'@'localhost' on all databases
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

-- Grant the 'SELECT' privilege to 'holberton_user'@'localhost' on the 'nexus6' table in the 'tyrell_corp' database
GRANT SELECT ON tyrell_corp.nexus6 TO holberton_user@localhost;

-- Grant the 'SELECT' privilege to 'holberton_user'@'localhost' on the 'user' table in the 'mysql' database
GRANT SELECT ON mysql.user TO holberton_user@localhost;

-- Grant the 'REPLICATION SLAVE' privilege to 'replica_user'@'%' on all databases
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

-- Reload the privilege tables to ensure that the new privileges take effect
FLUSH PRIVILEGES;
