# !/usr/bin/python
# -*- coding: utf-8 -*-

import SerialPortCore

class Method1Model:
    def __init__(self, port):
        self.view = None
        self.serialPortName = port

    def setView(self, view):
        self.view = view

    def turnOnMethod(self):
        mes = 'A'
        SerialPortCore.sendToComPort(self.serialPortName, message=mes)

    def turnOffMethod(self):
        mes = 'B'
        SerialPortCore.sendToComPort(self.serialPortName, message=mes)

    def inUpravlChoose(self):
        mes = 'C'
        SerialPortCore.sendToComPort(self.serialPortName, message=mes)

    def inUpravlSave(self):
        mes = 'D'
        SerialPortCore.sendToComPort(self.serialPortName, message=mes)
