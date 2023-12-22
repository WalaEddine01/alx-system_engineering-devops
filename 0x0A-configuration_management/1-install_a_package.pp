# installing flask from pip3, Using Puppet
package { 'flask':
  provider => 'pip3',
  ensure   => '2.1.0',
}
