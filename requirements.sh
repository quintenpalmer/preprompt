#!/bin/bash

ROOT_UID=0

if [ "$UID" -ne "$ROOT_UID" ]; then
	echo "this script requires to be run as root"
else
	distro="$(cat /etc/issue | xargs | cut -d ' ' -f 1)"
	if [ $distro == "Fedora" ]; then
		yum install python-pip
		pip install django
		yum install MySQL-python
		yum install mysql-server
		yum install mysql-connector-java
	elif [ $distro == "Ubuntu" ]; then
		apt-get install python-pip
		pip install django
		apt-get install python-mysqldb
		apt-get install mysql-server
		apt-get install java-mysqldb
	else
		echo "Unsupported Linux Distro"
	fi
fi
