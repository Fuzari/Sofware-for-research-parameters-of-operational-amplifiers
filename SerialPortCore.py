# !/usr/bin/python
# -*- coding: utf-8 -*-

import serial
import serial.tools.list_ports


def checkComPortAvailable(target):
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if port.device == target:
            serialPort = serial.Serial(port.device)
            if serialPort.isOpen():
                serialPort.baudrate = 1200
                serialPort.timeout = 0.2
                serialPort.stopbits = serial.STOPBITS_ONE
                serialPort.bytesize = serial.EIGHTBITS
                serialPort.parity = serial.PARITY_NONE
            else:
                serialPort = None
            break
        else:
            serialPort = None
    return serialPort


def sendToComPort(port, message):
    data = bytes(message, encoding='ascii')
    print(data)
    print(port)
    port.write(data)


def closeComPort(port):
    port.close()


