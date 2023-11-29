#isntall and configue nginx using puppet

exec {'install':
  provider => shell,
  command  => 'sudo apt-get -y update ; sudo apt-get install -y nginx ; echo "Hello World!" | sudo tee /var/www/html/index.html ; sudo sed -i "40i location /redirect_me {\nreturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n}\n" /etc/nginx/sites-available/default ;  sudo service nginx restart'
  }
