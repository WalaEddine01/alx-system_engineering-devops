# installing flask from pip3, Using Puppet
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
