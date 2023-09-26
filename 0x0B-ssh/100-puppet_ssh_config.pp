#!/usr/bin/env bash
# using puppet

file { '/etc/ssh/ssh_config':
	ensure => present,

content =>"
	host*
	PasswordAuthentication no
	IdentityFile ~/.ssh/school
	",
}
