# create a manifest that kills a process named killmenow, Using Puppet
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => ['/usr/sbin', '/usr/bin'],
}
