#insert customer header in the response

exec {'update':
  provider  => shell,
  command   => 'sudo apt -y update',
  logoutput => true,
  before    => Exec['nginx installation']
  }

exec { 'nginx installation':
  provider  => shell,
  command   => 'sudo apt -y install nginx',
  logoutput => true
  }

exec { 'custom_header':
  provider    => shell,
  environment => ["HOSTNAME=${hostname}"],
  command     => 'sudo sed -i "29i add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default',
  logoutput   => true,
  before      => Exec['start_nginx']
  }

exec { 'start_nginx':
  provider  => shell,
  command   => 'sudo service nginx restart',
  logoutput => true
  }
