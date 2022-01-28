#!/bin/sh

sudo apt-get install python3 apache2
pip install picamera urllib numpy RPi.GPIO

# copy ./website/* to apache web folder
