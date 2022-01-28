#!/bin/sh

echo install python3 and apache2
sudo apt-get install python3 apache2

echo install python packages/libarys
pip install picamera
pip install numpy
pip install RPi.GPIO

echo copy website to /var/www/html
#copy ./website/* to apache web folder
cp -a ../Website/* /var/www/html
