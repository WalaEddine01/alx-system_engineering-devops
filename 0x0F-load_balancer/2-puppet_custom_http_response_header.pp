package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('nginx/default.erb'),
  notify  => Exec['reload_nginx'],
}

exec { 'reload_nginx':
  command     => '/etc/init.d/nginx restart',
  refreshonly => true,
}
