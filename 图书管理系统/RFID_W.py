import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    text = input(':')
    print('0')
    reader.write(text)
    print('0')
finally:
    GPIO.cleadup()