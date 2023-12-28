#!/usr/bin/puppet
# installing flask from pip3

package {'python3-pip':
  ensure  => present,
}

# Install werkzeug package
package {'werkzeug':
  ensure   => '2.1.1',
  provider =>'pip3',
}

# Install flask package
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
