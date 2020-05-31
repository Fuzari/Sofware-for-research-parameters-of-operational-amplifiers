# !/usr/bin/python
# -*- coding: utf-8 -*-

import SerialPortCore


class Method4Model:
    def __init__(self, port):
        self.view = None
        self.serialPortName = port

    def setView(self, view):
        self.view = view

    def turnOnMethod(self):
        mes = 'M'
        SerialPortCore.sendToComPort(self.serialPortName, mes)

    def turnOffMethod(self):
        mes = 'B'
        SerialPortCore.sendToComPort(self.serialPortName, mes)

    def setChoose(self):
        mes = 'O'
        SerialPortCore.sendToComPort(self.serialPortName, mes)

    def setSave(self):
        mes = 'P'
        SerialPortCore.sendToComPort(self.serialPortName, mes)

    def setSigsIn2(self):
        mes = 'Q'
        SerialPortCore.sendToComPort(self.serialPortName, mes)

    def setSig1In1(self):
        mes = 'R'
        SerialPortCore.sendToComPort(self.serialPortName, mes)

    def changeSigsStates(self):
        mes = 'S'
        SerialPortCore.sendToComPort(self.serialPortName, mes)

    def setSigsIn1(self):
        mes = 'T'
        SerialPortCore.sendToComPort(self.serialPortName, mes)
