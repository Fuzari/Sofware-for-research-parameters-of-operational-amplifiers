# !/usr/bin/python
# -*- coding: utf-8 -*-

import SerialPortCore


class Method17Model:
    def __init__(self, port):
        self.view = None
        self.serialPortName = port

    def setView(self, view):
        self.view = view