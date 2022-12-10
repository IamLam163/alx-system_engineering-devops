# Create a manifest that kills a running process:

exec { 'pkill':
  command => 'pkill killmenow',
  path    => '/usr/local/bin/:/bin/',
}
