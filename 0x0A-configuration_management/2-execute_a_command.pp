# create a manifest that kills a process named killmenow, Using Puppet
exec {
  'killmenow':
  command => 'killall c',
  path    => '/bin:/usr/bin',
}
