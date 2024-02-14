#!/usr/bin/puppet
# This is a simple example of how to use the exec resource to run a command on the system.
$path_file = '/var/www/html/wp-settings.php'

exec { 'fix-wordpress':
  command => "sed -i 's/phpp/php/g' ${path_file}", # replace phpp with php
  path    => ['/usr/bin', '/bin', '/usr'] # or wherever sed is located
}
