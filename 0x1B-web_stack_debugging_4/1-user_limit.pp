# switch to holbeton user
user { 'holberton':
  ensure  => 'present',
}

file { '/etc/security/limits.conf':
  ensure  => 'file',
  content => "holberton hard nofile 65535\nholberton soft nofile 65535\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}
