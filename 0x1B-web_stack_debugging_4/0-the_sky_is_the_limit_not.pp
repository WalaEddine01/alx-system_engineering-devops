#!/usr/bin/env puppet
# this is a puppet script to fix the issue with the number of arguments

$path2 = '/var/www/html'

service { 'nginx':
  ensure => running,
  enable => true,
}

exec { 'fix_server':
  command => "/bin/sed -i 's|root /usr/share/nginx/html;|root ${path2};|' /etc/nginx/sites-available/default",
  path    => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
}
