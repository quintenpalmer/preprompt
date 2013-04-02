#!/bin/bash

find . -name "*.java" | xargs sed -i "s/import model/import ppbackend.model/g"
find . -name "*.java" | xargs sed -i "s/import control/import ppbackend.control/g"
find . -name "*.java" | xargs sed -i "s/package model/package ppbackend.model/g"
find . -name "*.java" | xargs sed -i "s/package control/package ppbackend.control/g"
