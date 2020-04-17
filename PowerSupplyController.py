# !/usr/bin/python
# -*- coding: utf-8 -*-


class PowerSupplyController:
    def __init__(self, model):
        self.model = model

    def printHello(self):
        print ("hello, I'm Controller!")
        self.model.sayHello()

    def checkWorkCall(self):
        self.model.checkWork()
        print("Controller's checkWorkCall implemented.")

    def setOutputCall(self, canal, voltage, amperage, limitAmperage):
        self.model.setOutput(canal=canal, voltage=voltage, amperage=amperage, limitAmperage=limitAmperage)
        print("Canal", canal)
        print("V", voltage)
        print("A", amperage)
        print("lim A", limitAmperage)
        print("Controller's setOutputCall implemented.")
