#Python 3.9.2 (default, Mar 12 2021, 04:06:34) 
#[GCC 10.2.1 20210110] on linux
#Type "help", "copyright", "credits" or "license()" for more information.
from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
led=40
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,GPIO.LOW)
reader = SimpleMFRC522()
try:
    while True:
        print ("hold a tag near the reader")
        id, text = reader.read()
        print (id)
        print (type(id))
        print(text)
        sleep(5)
except KeyboardInterrupt:
        GPIO.cleanup()
        raise
