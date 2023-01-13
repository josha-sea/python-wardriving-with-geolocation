# Python WIFI-geolocation mapping tool

## Motivation
### Ever wanted a database with the wifis of your area mapped to geolocation? <br>
You came to the right place. <br>
This script is inspired by the concept of wardriving and a certain curiosity.

## Description
A commandline-script written in Python that scans nearby wifi-access-points and stores them in a SQLite database with geolocation. <br>
Tested on Windows 10.

## Installing / Compiling
### What you need:

- Download or clone the git repo:
<pre> <code> git clone https://github.com/josha-sea/python-wifi-mapping-tool.git</code> </pre>
- A laptop
- A gps-module that feeds NMEA-data to the script. Tested with this module from AliExpress: G-Mouse VK-162 (no affilliation)


## Usage
After cloning or downloading the git repo, open a shell in the directory:

- Install the requirements.txt
<pre> <code>pip install -r requirements.txt</code> </pre>

- Find out the COM-port of your GPS-module and remember it. You will be promted to input the number.

- Start the script:
<pre> <code>python main.py</code> </pre>

The paths to the database-directory and logs-directory will be shown and the scannin' and mappin' will start.
Have fun!

by Josha Sea