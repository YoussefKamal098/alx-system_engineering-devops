## Documentation for Setting Up SSL/TLS Certificates with Certbot and HAProxy

This documentation provides a step-by-step guide to setting up SSL/TLS certificates for a domain using Certbot and integrating them with HAProxy.

### Commands and Their Descriptions

1. **Update Package Lists**
    ```sh
    sudo apt update
    ```
    - **Description**: Updates the package lists for upgrades and new package installations. This ensures that you are working with the latest versions available in the repositories.

2. **Install Snapd (Optional)**
    ```sh
    sudo apt install snapd
    ```
    - **Description**: Installs `snapd`, a package manager for installing snap packages. Snap packages are containerized software packages that work across many different Linux distributions. This step is optional if you prefer using snap packages for Certbot.

3. **Install Certbot**
    ```sh
    sudo apt-get install certbot
    ```
    - **Description**: Installs the latest version of Certbot via `apt`. Certbot is a tool for automating the issuance and renewal of SSL/TLS certificates from Let's Encrypt.

4. **Stop HAProxy Service**
    ```sh
    sudo service haproxy stop
    ```
    - **Description**: Stops the HAProxy service to free up port 80 for Certbot's standalone mode, which is necessary to complete the HTTP-01 challenge.

5. **Obtain SSL/TLS Certificates using Certbot**
    ```sh
    sudo certbot certonly --standalone --preferred-challenges http --http-01-port 80 -d www.example.com
    ```
    - **Description**: Obtains SSL/TLS certificates for the domain `www.example.com` using Certbot in standalone mode.
    - **Options**:
        - `certonly`: Obtain the certificate only without configuring a web server.
        - `--standalone`: Use Certbot's built-in web server for the HTTP-01 challenge.
        - `--preferred-challenges http`: Use HTTP-01 challenge for domain validation.
        - `--http-01-port 80`: Use port 80 for the HTTP-01 challenge.
        - `-d www.example.com`: Specify the domain to obtain the certificate for.

6. **List Certificate Directory**
    ```sh
    sudo ls /etc/letsencrypt/live/www.example.com
    ```
    - **Description**: Lists the contents of the certificate directory for the domain to verify the certificate files were created successfully.

7. **Create Directory for HAProxy Certificates**
    ```sh
    sudo mkdir -p /etc/haproxy/certs
    ```
    - **Description**: Creates a directory to store the combined certificate and private key files for HAProxy.

8. **Combine Certificate and Private Key for HAProxy**
    ```sh
    DOMAIN='www.example.com' sudo -E bash -c 'cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/haproxy/certs/$DOMAIN.pem'
    ```
    - **Description**: Combines the certificate and private key into a single file for HAProxy.
    - **Options**:
        - `DOMAIN='www.example.com'`: Sets the domain environment variable.
        - `sudo -E bash -c`: Runs the command with elevated privileges, preserving the environment variable.
        - `cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/haproxy/certs/$DOMAIN.pem`: Combines the full chain certificate and the private key into a single file.

9. **Set Permissions for Certificate Directory**
    ```sh
    sudo chmod -R go-rwx /etc/haproxy/certs
    ```
    - **Description**: Sets restrictive permissions on the HAProxy certificates directory to ensure only the owner can read/write. This enhances security by preventing unauthorized access.

10. **Generate a Diffie-Hellman Group**
    ```sh
    sudo openssl dhparam -out /etc/haproxy/dhparams.pem 2048
    ```
    - **Description**: Generates a Diffie-Hellman group for enhanced security in SSL/TLS handshakes. This helps in preventing SSL key exchange vulnerabilities.

11. **Edit HAProxy Configuration**
    ```sh
    sudo vi /etc/haproxy/haproxy.cfg
    ```
    - **Description**: Opens the HAProxy configuration file in the `vi` editor for editing. Add the necessary configuration to use the new SSL/TLS certificates and the Diffie-Hellman group.

12. **Verify HAProxy Configuration**
    ```sh
    sudo haproxy -f /etc/haproxy/haproxy.cfg -c
    ```
    - **Description**: Verifies the syntax of the HAProxy configuration file to ensure there are no errors before restarting the service.

13. **Start HAProxy Service**
    ```sh
    sudo service haproxy start
    ```
    - **Description**: Starts the HAProxy service with the new configuration, enabling it to serve HTTPS traffic using the newly obtained certificates.

### Example Configuration Addition for HAProxy

Here is a full example of an `haproxy.cfg` configuration file that integrates the new SSL/TLS certificates:

```haproxy
global
    log /dev/log    local0
    log /dev/log    local1 notice
    chroot /var/lib/haproxy
    stats socket /run/haproxy/admin.sock mode 660 level admin expose-fd listeners
    stats timeout 30s
    user haproxy
    group haproxy
    daemon
    ssl-dh-param-file /etc/haproxy/dhparams.pem

defaults
    log     global
    mode    http
    option  httplog
    option  dontlognull
    timeout connect 5000
    timeout client  50000
    timeout server  50000
    errorfile 400 /etc/haproxy/errors/400.http
    errorfile 403 /etc/haproxy/errors/403.http
    errorfile 408 /etc/haproxy/errors/408.http
    errorfile 500 /etc/haproxy/errors/500.http
    errorfile 502 /etc/haproxy/errors/502.http
    errorfile 503 /etc/haproxy/errors/503.http
    errorfile 504 /etc/haproxy/errors/504.http

frontend www-frontend
    bind *:80
    bind *:443 ssl crt /etc/haproxy/certs/www.example.com.pem
    redirect scheme https code 301 if !{ ssl_fc }
    default_backend www-backend

backend www-backend
    balance roundrobin
    server web1 192.168.1.1:80 check
    server web2 192.168.1.2:80 check
```

### Summary

This guide walks you through installing necessary packages, obtaining SSL/TLS certificates using Certbot, combining the certificate and private key for HAProxy, generating a Diffie-Hellman group, setting appropriate permissions,
and configuring HAProxy to use the new certificates.
Replace `www.example.com` with your actual domain name.
