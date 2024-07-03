# # Seting up my client config file
# include stdlib
#
# file_line { 'Turn off passwd auth':
#   ensure => present,
#   path   => '/etc/ssh/ssh_config',
#   line   => '    PasswordAuthentication no',
#   replace => true,
# }
#
# file_line { 'Delare identity file':
#   ensure => present,
#   path   => '/etc/ssh/ssh_config',
#   line   => '     IdentityFile ~/.ssh/school',
#   replace => true,
# }

# Changes SSH config file
exec { 'echo':
  path    => 'usr/bin:/bin',
  command => 'echo "    IdentityFile ~/.ssh/school\n    PasswordAuthentication no" >> /etc/ssh/ssh_config',
  returns => [0,1],
}
