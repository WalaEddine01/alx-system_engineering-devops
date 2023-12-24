# installing flask from pip3
package {
  'flask':
  ensure   => 'present',
  provider => 'pip3',
}
