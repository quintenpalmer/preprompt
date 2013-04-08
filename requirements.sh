#!/bin/bash

ROOT_UID=0

if [ "$UID" -ne "$ROOT_UID" ]; then
	echo "this script requires to be run as root"
else
	apt-get install python-pip
	pip install django
	apt-get install python-mysqldb
	#apt-get install java-mysqldb
	apt-get install mysql-server
fi
