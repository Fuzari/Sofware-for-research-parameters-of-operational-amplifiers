# !/usr/bin/python
# -*- coding: utf-8 -*-

import pyvisa


class PowerSupplyModel:
    def setView(self, view):
        self.view = view

    def sayHello(self):
        print ("Hello, I'm model!")
        self.view.sayHello()

    def checkWork(self):
        rm = pyvisa.ResourceManager()
        powerSupply = rm.open_resource("GPIB0::14::INSTR")  # Здесь необходим идентификатор Источника напряжения
        powerSupply.write('*IDN?')
        ans = powerSupply.read()
        self.view.checkWorkAnswer(ans=ans)
        print("Model's checkWork implemented.")

    def setOutput(self, canal, voltage, amperage, limitAmperage):
        rm = pyvisa.ResourceManager()
        powerSupply = rm.open_resource("GPIB0::14::INSTR")  # Здесь необходим идентификатор Источника напряжения
        powerSupply.write(':INST ' + canal)
        powerSupply.write(':CURR ' + amperage)
        powerSupply.write(':CURR:PROT ' + limitAmperage)
        powerSupply.write(':CURR:PROT:STAT ON')
        powerSupply.write(':VOLT' + voltage)
        powerSupply.write(':OUTPT ' + canal + ',ON')
        ans = "output"
        self.view.setOutputAnswer(ans=ans)
        print("Model's setOutput implemented.")

    def setTrackingTo(self, canal):
        rm = pyvisa.ResourceManager()
        powerSupply = rm.open_resource("GPIB0::14::INSTR")  # Здесь необходим идентификатор Источника напряжения
        powerSupply.write(':OUTPT:TRAC ' + canal + ',ON')
        ans = 'Tracking'
        self.view.setTrackingAnswer(ans=ans)
        print("Model's setTrackingTo implemented.")