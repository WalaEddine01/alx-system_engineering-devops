package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => file,
  content => "Hello World!\n",
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('nginx/default.erb'),
}

exec { 'restart_nginx':
  command     => '/etc/init.d/nginx restart',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}
