from time import sleep
import serial
ser=serial.Serial("com4",115200,timeout=0.5)
ser.baudrate=115200
ser.port='COM4'
while True:
    s=input(':')
    ser.write(s.encode())
    sleep(5)