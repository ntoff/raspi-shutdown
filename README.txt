Shutdown button for Raspberry Pi 2 model B (tested on my rpi2b v1.1).

***WARNING. IMPROPER USE MAY DAMAGE THE RASPBERRY PI PERNANENTLY.***

Use of this script is without warranty, any and all responsibility for its usage is upon the end user. 

This script is intended for use with EXTERNAL pull down and current limiting resistors. 
It does NOT enable any internal pullup or pulldown resistors if they may or may not even exist.
DO NOT CONNECT A SWITCH DIRECTLY TO THE RASPBERRY PI GPIO PINS.

To install the script download it to the raspberry pi and add it to the cron jobs (sudo crontab -e)
with the following: @reboot sudo python /path/to/script/raspi_shutdown.py &

To install the hardware: 
connect one leg of a 10k ohm resistor to ground
connect one leg of a 1k ohm resistor to the gpio port (pin #7 in this script)
connect one wire of a normally open momentary pushbutton switch to 3v3 (DO NOT ACCIDENTALLY CONNECT IT TO THE 5v PIN)
connect the two remaining legs of the resistors together along with the remaining wire from the switch.

It forms a voltage divider of sorts, 10k resistor pulls pin 7 to ground so it doesn't "float" during normal operation, the switch pulls pin 7 high through the 1k resistor when closed, calling for the pi to shutdown.

Any and all damage arising from the use or misuse of this information is wholly your responsibility. 