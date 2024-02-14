$path_file = '/var/www/html/wp-settings.php'

exec { 'replace_string':
  command => " -i 's/phpp/php/g' ${path_file}", # replace phpp with php
  path    => ['/usr/bin', '/bin', '/usr'] # or wherever sed is located
}
