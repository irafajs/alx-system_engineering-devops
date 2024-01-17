#fix the 500 error message
file { '/var/www/html/wp-settings.php':
  ensure  => file,
  content => inline_template("<%= File.read('/var/www/html/wp-settings.php').gsub('class-wp-locale.phpp', 'class-wp-locale.php') %>"),
  notify  => Service['apache2'],
}

service { 'apache2':
  ensure => 'running',
}
