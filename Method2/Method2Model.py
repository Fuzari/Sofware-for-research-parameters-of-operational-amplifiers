# !/usr/bin/python
# -*- coding: utf-8 -*-

import SerialPortCore


class Method2Model:
    def __init__(self, port):
        self.view = None
        self.serialPortName = port

    def setView(self, view):
        self.view = view

    def turnOnMethod(self):
        mes = 'E'
        SerialPortCore.sendToComPort(self.serialPortName, mes)

    def turnOffMethod(self):
        mes = 'F'
        SerialPortCore.sendToComPort(self.serialPortName, mes)

    def setSig1(self):
        mes = 'G'
        SerialPortCore.sendToComPort(self.serialPortName, mes)

    def setSig2(self):
        mes = 'H'
        SerialPortCore.sendToComPort(self.serialPortName, mes)
