# Puppet script to modify the maximum open files limit for Nginx

# Execute a command to update the maximum open files limit and restart Nginx
exec { 'modify nginx max open files limit':
  # Command to find and replace the current limit of 15 with 4096 in the Nginx configuration file
  command => 'sed -i "s/^ULIMIT=\"-n 15\"$/ULIMIT=\"-n 4096\"/" /etc/default/nginx && sudo service nginx restart',

  # Specify the search path for the 'sed' command and other utilities used in the command
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}
