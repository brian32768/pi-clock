# pi-clock

= Hardware

Pi Zero W
Pimoroni Inky pHAT (red/black/white version) Display size is 
SD card
USB cable + phone charger

Later on
beeper
push buttons
LEDs
Li-Ion battery and boost voltage regulator

= Software

Raspian Stretch
adafruit-blinka
Pyton Image Library

I am writing the code on a Mac and testing there. Output is to a file.

The concept here is to take advantage of the nonvolatile Inky display by updating the display
and then sleeping for a minute in a low power state to extend battery life.

= Bells and whistles aka Feature Creep

add alarm clock feature

add Bluetooth and WiFi presence detection

add weather information via Internet

add phases of moon

I guess the clock should check for config changes when it's awake? put them on Bellman?

= Setting up dev environment

I'm using virtualenvwrapper these days.

pip3 install PIL

showtime.py will generate a PNG file once per minute that simulates the image that will be sent to Inky.

