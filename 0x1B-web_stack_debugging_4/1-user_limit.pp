# Define an Exec resource named 'OS security config'
exec {'OS security config':
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}

# # Define an Exec resource named 'OS security config'
# exec {'OS security config':
#   # The command to be executed. This uses `sed` to find and replace 'holberton' with 'foo' in the /etc/security/limits.conf file
#   command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
#
#   # Specify the path where the command will look for executable files
#   path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/',
#
#   # Ensure that the command is run only if the resource is not already applied
#   # This ensures idempotency, meaning running the script multiple times will have the same effect as running it once
#   unless  => 'grep -q "foo" /etc/security/limits.conf',
#
#   # Notify that this resource should be re-applied if there are changes to the '/etc/security/limits.conf' file
#   notify  => Exec['reload_security_config'],
# }
#
# # Define another Exec resource to reload security configuration if the previous resource changes the file
# exec {'reload_security_config':
#   # Command to reload the security configuration. This can be any command required to apply changes.
#   command => 'echo "Reloading security configuration"',
#
#   # Path specification similar to the previous resource
#   path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/',
#
#   # Ensure this command runs after the 'OS security config' resource
#   subscribe => Exec['OS security config'],
# }
