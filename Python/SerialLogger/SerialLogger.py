import serial
ser = serial.Serial(port="/dev/ttyACM1", baudrate=9600)
ser.flushInput()

while True:
    f = open("Python/SerialLogger/data/data.txt", "a")
    ser_bytes = ser.readline()
    data = str(ser_bytes)
    f.write(data)
    f.write("\n")
    f.close()

    print(ser_bytes)