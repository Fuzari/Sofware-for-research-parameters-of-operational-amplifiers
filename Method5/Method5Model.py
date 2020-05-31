# !/usr/bin/python
# -*- coding: utf-8 -*-

import SerialPortCore


class Method5Model:
    def __init__(self, port):
        self.view = None
        self.serialPortName = port

    def setView(self, view):
        self.view = view

    def turnOnMethod(self):
        mes = 'U'
        SerialPortCore.sendToComPort(self.serialPortName, mes)

    def turnOffMethod(self):
        mes = 'B'
        SerialPortCore.sendToComPort(self.serialPortName, mes)
