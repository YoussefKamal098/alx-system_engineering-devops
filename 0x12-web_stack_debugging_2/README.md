### Understanding and Configuring Nginx and User Accounts

#### Part 1: Explaining the Nginx Configuration File

Here’s a detailed explanation of each line in the given Nginx configuration file:

```nginx
user www-data;
worker_processes auto;
pid /run/nginx.pid;
error_log /var/log/nginx/error.log;
include /etc/nginx/modules-enabled/*.conf;

events {
    worker_connections 768;
    # multi_accept on;
}

http {

    ##
    # Basic Settings
    ##

    sendfile on;
    tcp_nopush on;
    types_hash_max_size 2048;
    # server_tokens off;

    
    server_names_hash_bucket_size 64;
    # server_name_in_redirect off;

    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    ##
    # SSL Settings
    ##

    ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3; # Dropping SSLv3, ref: POODLE
    ssl_prefer_server_ciphers on;

    ##
    # Logging Settings
    ##

    access_log /var/log/nginx/access.log;

    ##
    # Gzip Settings
    ##

    gzip on;

    # gzip_vary on;
    # gzip_proxied any;
    # gzip_comp_level 6;
    # gzip_buffers 16 8k;
    # gzip_http_version 1.1;
    # gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

    ##
    # Virtual Host Configs
    ##

    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*;
}


#mail {
#    # See sample authentication script at:
#    # http://wiki.nginx.org/ImapAuthenticateWithApachePhpScript
#
#    # auth_http localhost/auth.php;
#    # pop3_capabilities "TOP" "USER";
#    # imap_capabilities "IMAP4rev1" "UIDPLUS";
#
#    server {
#        listen     localhost:110;
#        protocol   pop3;
#        proxy      on;
#    }
#
#    server {
#        listen     localhost:143;
#        protocol   imap;
#        proxy      on;
#    }
#}
```

- **`user www-data;`**: This sets the user and group under which the Nginx worker processes will run. The user `www-data` is typically used for web services in Debian-based systems.
- **`worker_processes auto;`**: This directive configures the number of worker processes. Using `auto` allows Nginx to automatically adjust this number based on the number of available CPU cores.
- **`pid /run/nginx.pid;`**: Specifies the file where the process ID of the Nginx master process is stored.
- **`error_log /var/log/nginx/error.log;`**: Defines the file where Nginx will log errors.
- **`include /etc/nginx/modules-enabled/*.conf;`**: Includes additional configuration files for Nginx modules.

**Events Block:**
- **`worker_connections 768;`**: Sets the maximum number of simultaneous connections that can be opened by a worker process.

**HTTP Block:**
- **`sendfile on;`**: Enables the use of `sendfile()` for transferring files, which is more efficient.
- **`tcp_nopush on;`**: Optimizes the way data is sent over the network.
- **`types_hash_max_size 2048;`**: Sets the maximum size of the types hash tables.
- **`server_names_hash_bucket_size 64;`**: Sets the bucket size for the server names hash tables.

- **`include /etc/nginx/mime.types;`**: Includes the file defining MIME types.
- **`default_type application/octet-stream;`**: Sets the default MIME type for files.

**SSL Settings:**
- **`ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;`**: Specifies the SSL/TLS protocols that are enabled.
- **`ssl_prefer_server_ciphers on;`**: Ensures the server's cipher preference is used.

**Logging Settings:**
- **`access_log /var/log/nginx/access.log;`**: Specifies the file where access logs are stored.

**Gzip Settings:**
- **`gzip on;`**: Enables gzip compression for responses.

**Virtual Host Configs:**
- **`include /etc/nginx/conf.d/*.conf;`**: Includes additional configuration files for virtual hosts.
- **`include /etc/nginx/sites-enabled/*;`**: Includes configuration files for sites enabled on the server.

**Mail Block (Commented Out):**
- This section includes configurations for mail proxying, which are currently commented out.

#### Part 2: Running Nginx as a Different User

The command `su nginx -s /bin/bash -c 'service nginx restart'` switches to the `nginx` user and restarts the Nginx service. Here’s a breakdown:
- **`su nginx`**: Switches to the `nginx` user.
- **`-s /bin/bash`**: Specifies the shell to use, in this case, `/bin/bash`.
- **`-c 'service nginx restart'`**: Executes the command to restart Nginx.

If you attempt to run Nginx as a user different from the one specified in the configuration file (`www-data` in this case), you may encounter permission issues, as the Nginx worker processes would not have the necessary permissions to access certain files and directories configured for `www-data`.

#### Part 3: Using the `getent` Command

The `getent` command retrieves entries from administrative databases, which can be useful for verifying user information.

**Syntax:**
```bash
getent [database] [key ...]
```

**Example: Querying the `passwd` Database for User Information**
```bash
getent passwd www-data
```

**Explanation:**
- **`passwd`**: Specifies the password database.
- **`www-data`**: The username to look up.

**Output:**
```
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
```

**Fields in Output:**
1. **Username**: `www-data`
2. **Password**: `x` (password stored in `/etc/shadow`)
3. **User ID (UID)**: `33`
4. **Group ID (GID)**: `33`
5. **User ID Info (GECOS)**: `www-data`
6. **Home Directory**: `/var/www`
7. **Shell**: `/usr/sbin/nologin`

This command helps verify if a user like `www-data` exists and retrieves their account details.

### Changing Nginx User and Listening Port

To run Nginx as a different user and change the listening port to 8080, follow these steps:

1. **Change User in Nginx Configuration:**
   Edit the Nginx configuration file (e.g., `/etc/nginx/nginx.conf`) and change the `user` directive:
   ```nginx
   user newuser;
   ```

2. **Create the User if It Doesn't Exist:**
   If the new user doesn't exist, create it using:
   ```bash
   sudo useradd -r -d /var/www -s /usr/sbin/nologin newuser
   ```

3. **Change the Listening Port:**
   Edit the server block in the configuration file to listen on port 8080:
   ```nginx
   server {
       listen 8080;
       ...
   }
   ```

4. **Restart Nginx:**
   Restart Nginx to apply the changes:
   ```bash
   sudo systemctl restart nginx
   ```

**Verifying User with `getent`:**
Use `getent` to verify the new user:
```bash
getent passwd newuser
```

By following these steps, you can run Nginx under a different user and change the listening port, ensuring that the server operates with the correct permissions and configurations.
