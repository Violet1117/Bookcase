import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import re
from threading import Thread

rfid = 0
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN,GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)
p.start(2.5)
reader = SimpleMFRC522()


def data():
    global rfid
    while True:
        id, text = reader.read()
        clean_text = re.findall('\d+', text)
        match = int(clean_text[0])
        rfid = match

def lock():
    global rfid
    while True:
        print("rfid=", rfid)
        if rfid == 1234:
            p.ChangeDutyCycle(2.5)
            time.sleep(3)
            rfid = 0
        else:
            p.ChangeDutyCycle(10)
            time.sleep(0.5)

try:
    if __name__ == "__main__":
        t1 = Thread(target=data)
        t2 = Thread(target=lock)
        t1.start()
        t2.start()

except:
    p.stop()
    GPIO.cleanup()