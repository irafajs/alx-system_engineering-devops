# increase ulimit number
exec { 'fix-ulimit':
  command => "/bin/sed -i 's/15/4096/' /etc/default/nginx",
  path    => ['/bin', '/usr/bin'],
}

# nginx restart
exec { 'nginx-restart':
  command     => '/etc/init.d/nginx restart',
  path        => '/etc/init.d',
  refreshonly => true,
  subscribe   => Exec['fix-ulimit'],
}
