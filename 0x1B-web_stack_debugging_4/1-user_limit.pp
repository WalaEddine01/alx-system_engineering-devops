#!/usr/bin/env puppet
# Puppet manifest to login with the holberton user and
# open a file without any error message.

exec { 'hard_limit':
  command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 4000/g" /etc/security/limits.conf',
  path    => '/bin',
}

exec { 'soft_limit':
  command => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 4000/g" /etc/security/limits.conf',
  path    => '/bin',
}
