#install configure nginx using puppet

exec { 'check-update-linux':
  command => 'sudo apt-get -y update',
  }

exec { 'install-nginx':
  command => 'sudo apt-get install -y nginx',
  require => Exec['check-update-linux']
  }

exec { 'create-index-html':
  command => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  require => Exec['install-nginx']
  }

exec { 'redirectioning':
  command => 'sed -i "40i location /redirect_me {\nreturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n}\n" /etc/nginx/sites-available/default',
  require => Exec['install-nginx'],
  }

exec { 'restart-nginx':
  command => 'service nginx restart',
  require => Exec['redirectioning']
  }
