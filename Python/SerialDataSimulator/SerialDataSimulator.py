import serial
import os
import time

serialPort = '/dev/tnt0'

ser = serial.Serial(port='/dev/tnt0', baudrate=9600, bytesize=8, parity=serial.PARITY_EVEN, stopbits=1)  # open serial port
vserial1 = serial.Serial(port='/dev/tnt1', baudrate=9600, bytesize=8, parity=serial.PARITY_EVEN, stopbits=1)
print(ser.name)         # check which port was really used

while True:
    with open('data.txt', 'r') as f:
        for line in f:
            line = bytes(line, 'utf-8')
            print(line)
            ser.write(line)     # write a string
            os.system('echo > ' + serialPort)
            time.sleep(0.3)





ser.close()             # close port


# Serial.write(b"testi")
