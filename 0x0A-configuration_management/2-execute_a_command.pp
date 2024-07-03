# Manifest that kills a process named killmenow.

exec {  'pkill':
    path    => '/usr/bin:/bin',
    command => 'pkill  killmenow',
}
