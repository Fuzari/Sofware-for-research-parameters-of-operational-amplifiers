# !/usr/bin/python
# -*- coding: utf-8 -*-

import SerialPortCore


class Method3Model:
    def __init__(self, port):
        self.view = None
        self.serialPortName = port

    def setView(self, view):
        self.view = view

    def turnOnMethod(self):
        mes = 'I'
        SerialPortCore.sendToComPort(self.serialPortName, mes)

    def turnOffMethod(self):
        mes = 'J'
        SerialPortCore.sendToComPort(self.serialPortName, mes)

    def setSig1Sig2(self):
        mes = 'K'
        SerialPortCore.sendToComPort(self.serialPortName, mes)

    def offSig1Sig2(self):
        mes = 'L'
        SerialPortCore.sendToComPort(self.serialPortName, mes)
