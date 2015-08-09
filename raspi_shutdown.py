# Script uses the BOARD pin numbering.
# see http://www.element14.com/community/docs/DOC-73950/l/raspberry-pi-2-model-b-gpio-40-pin-block-pinout
# for numbers
#
# CAUTION! IMPROPER USE CAN DAMAGE THE RASPBERRY PI!
# THIS SCRIPT IS DESIGNED TO BE USED WITH EXTERNAL CURRENT LIMITING AND PULL DOWN RESISTORS.
# DO NOT CONNECT A SWITCH DIRECTLY TO THE RASPI AS IS THE CASE WITH OTHER SHUTDOWN SCRIPTS
# AS THIS MAY CAUSE A SHORT CIRCUIT AND DAMAGE THE PI PERMANENTLY.

import RPi.GPIO as GPIO
from subprocess import call

shutdown_pin=7 # GPIO pin to use to detect a button push.

GPIO.setmode(GPIO.BOARD) # set the pin numbering to the board numbering system.
GPIO.setup(shutdown_pin, GPIO.IN) # set the required pin to an input pin

try:
    GPIO.wait_for_edge(shutdown_pin, GPIO.RISING) # wait for the shutdown pin to be pulled high (3v3)
    call('halt', shell=False)
except:
    pass
finally:
    GPIO.cleanup()
