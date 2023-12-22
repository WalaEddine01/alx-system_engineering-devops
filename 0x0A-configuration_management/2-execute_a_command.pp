# create a manifest that kills a process named killmenow, Using Puppet
exec { 'kill':
  command => 'pkill -f killmenow',
}
