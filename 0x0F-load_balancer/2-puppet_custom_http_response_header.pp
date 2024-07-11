# This is a Puppet manifest file

# Update package lists
exec { 'update':  # Defines a resource of type 'exec' with a name 'update'
  command  => 'sudo apt-get update',  # Specifies the command to be executed, which updates package lists
  provider => shell,  # Sets the provider to 'shell' to execute the command using the system shell
}

# Install nginx package
package { 'nginx':  # Defines a resource of type 'package' with a name 'nginx'
  ensure  => installed,  # Sets the desired state of the package to 'installed'
  require => Exec['update'],  # Declares a dependency on the 'update' resource, ensuring package lists are updated before installing nginx
}

# Add custom header to nginx configuration
file_line { 'headercustom':  # Defines a resource of type 'file_line' with a name 'headercustom'
  ensure  => present,  # Sets the desired state of the line to 'present' (meaning it should exist)
  path    => '/etc/nginx/sites-available/default',  # Specifies the path to the file where the line will be added
  after   => ':80 default_server;',  # Defines the line after which the new line will be inserted (after ':80 default_server;')
  line    => "add_header X-Served-By \"${hostname}\";",  # Defines the content of the new line, adding a custom header with the server's hostname
  require => Package['nginx'],  # Declares a dependency on the 'nginx' package resource, ensuring nginx is installed before adding the configuration line
}

# Start and manage the nginx service
service { 'nginx':  # Defines a resource of type 'service' with a name 'nginx'
  ensure  => running,  # Sets the desired state of the service to 'running'
  require => File_line['headercustom'],  # Declares a dependency on the 'headercustom' resource, ensuring the custom header is added before starting the service
}
