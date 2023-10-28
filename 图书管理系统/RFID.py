import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
def read():
    while text!='':
        id,text = SimpleMFRC522().read()
        print("rfid=",text)
        time.sleep(1)