#!/usr/bin/puppet
# Using Puppet make changes to our configuration file
# to connect to a server without typing a password.

file { '/etc/ssh/ssh_config':
ensure  => file,
content => template('2-ssh_config')
}
