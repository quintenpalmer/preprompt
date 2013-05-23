#!/bin/bash

ROOT_UID=0

if [ "$UID" -ne "$ROOT_UID" ]; then
	echo "this script requires to be run as root"
else
	distro="$(cat /etc/issue | xargs | cut -d ' ' -f 1)"
	if [ $distro == "Fedora" ]; then
		# MYSQL
		yum install mysql-server
		# PYTHON
		yum install python-pip
		pip install django
		yum install MySQL-python
		# GO
		yum install go
		go get github.com/ziutek/mymysql/godrv

	elif [ $distro == "Ubuntu" ]; then
		# MYSQL
		apt-get install mysql-server
		# PYTHON
		apt-get install python-mysqldb
		apt-get install python-pip
		pip install django
		# GO
		apt-get install golang
		go get github.com/ziutek/mymysql/godrv

	else
		echo "Unsupported Linux Distro"
	fi
fi
