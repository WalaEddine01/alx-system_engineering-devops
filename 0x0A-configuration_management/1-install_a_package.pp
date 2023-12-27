# installing flask from pip3
# Ensure Python 3.8.10
package { 'python3':
ensure   => '3.8.10',
provider => 'apt',
}
# Ensure pip3
package { 'python3-pip':
ensure  => 'present',
require => Package['python3'],
}
# Installing Werkzeug
package { 'Werkzeug':
ensure   => '2.1.1',
provider => 'pip3',
require  => Package['python3-pip']
}
# Installing flask
package { 'Flask':
ensure   => '2.1.0',
provider => 'pip3',
require  => Package['python3-pip'],
}
