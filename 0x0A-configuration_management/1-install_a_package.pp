# installing flask from pip3
# Ensure Python 3.8.10
package { 'python3':
ensure => 'installed',
}
# Ensure pip3
package { 'python3-pip':
ensure  => 'present',
require => Package['python3'],
}
# Installing Werkzeug
package { ['Werkzeug', 'Flask']:
ensure   => 'latest',
provider => 'pip3',
require  => Package['python3-pip'],
}
