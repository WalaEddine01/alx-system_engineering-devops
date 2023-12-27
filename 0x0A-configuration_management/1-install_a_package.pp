# installing flask from pip3
# Ensure Python 3.8.10
package { 'python3':
ensure => '3.8.10',
}
# Installing Flask
package { ['Flask']:
ensure   => '2.1.0',
provider => 'pip3',
require  => Package['python3-pip'],
}
# Installing Werkzeug
package { ['Werkzeug']:
ensure   => '2.1.1',
provider => 'pip3',
require  => Package['python3-pip'],
}
