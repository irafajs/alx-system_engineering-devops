#ssh_config.pp

file { '/home/vagrant/.ssh/config':
  ensure  => present,
  mode    => '0600',
  owner   => 'vagrant',
  group   => 'vagrant',
  content => "
    Host *
      IdentityFile /home/vagrant/.ssh/school
      PasswordAuthentication no
  "
  }
