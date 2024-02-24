#Using puppet, install flask from pip3.
#This manifest install Flask version 2.1.0 Using pip3

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
