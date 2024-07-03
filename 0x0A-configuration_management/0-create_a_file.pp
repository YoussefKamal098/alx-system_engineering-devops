# reate a file in /tmp.

file { 'school':
    path    => '/tmp/school',
    content => 'I love Puppet',
    mode    => '0744',
    user    => www-data,
    group   => 'www-data',
}
