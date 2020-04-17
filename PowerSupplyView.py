# !/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
from ttk import Frame, Button, Label, Combobox


class PowerSupplyView(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        # Common
        self.textFrame = Text(self, width=40, height=10)

        # CV output
        self.outputList = Combobox(self, height=30, width=5)
        self.voltageEntry = Entry(self, width=5)
        self.amperageEntry = Entry(self, width=5)
        self.limitEntry = Entry(self, width=5)
        self.voltageList = Combobox(self, height=30, width=3)
        self.amperageList = Combobox(self, height=30, width=3)
        self.limitAmperageList = Combobox(self, height=30, width=3)
        self.trackFunList = Combobox(self, height=30, width=5)

        self.initUI()

    def initUI(self):
        # Configuring a frame
        self.parent.title('Rigol DP832A control menu')
        self.pack(fill=BOTH, expand=True)

        # Creating a label to text field
        fieldLabel = Label(self, text='Event field')
        fieldLabel.place(x=2, y=2)

        # Configuring a text field for getting messages from equipment
        self.textFrame.place(x=2, y=25)

        # Configuring a "Clear" button
        clearButton = Button(self, text='Clear', command=self.clearTextField)
        clearButton.place(x=2, y=185)

        # Configuring a "Check work" button
        checkButton = Button(self, text='Check work', command=self.clearTextField)
        checkButton.place(x=90, y=185)

        # Setting CV output
        outputLabel = Label(self, text='Setting CV output')
        outputLabel.place(x=2, y=220)

        self.outputList.place(x=2, y=240)
        self.outputList['values'] = ('CH1', 'CH2', 'CH3')

        voltageLabel = Label(self, text='Enter voltage:')
        voltageLabel.place(x=2, y=275)

        amperageLabel = Label(self, text='Enter amperage:')
        amperageLabel.place(x=2, y=305)

        limitLabel = Label(self, text='Enter overcurrent\n protection limit:')
        limitLabel.place(x=2, y=335)

        self.voltageEntry.place(x=120, y=270)
        self.amperageEntry.place(x=120, y=300)
        self.limitEntry.place(x=120, y=340)

        setCVButton = Button(self, text='Set CV output', command=self.clearTextField)
        setCVButton.place(x=2, y=380)

        self.voltageList.place(x=180, y=273)
        self.voltageList['values'] = ('V', 'mV', 'uV', 'nV')
        self.voltageList.current(0)

        self.amperageList.place(x=180, y=303)
        self.amperageList['values'] = ('A', 'mA', 'uA', 'nA')
        self.amperageList.current(0)

        self.limitAmperageList.place(x=180, y=343)
        self.limitAmperageList['values'] = ('A', 'mA', 'uA', 'nA')
        self.limitAmperageList.current(0)

        # Setting track function
        trackLabel = Label(self, text='Set track function\n to output:')
        trackLabel.place(x=250, y=220)

        self.trackFunList.place(x=250, y=260)
        self.trackFunList['values'] = ('CH1', 'CH2')

        trackButton = Button(self, text='Set', command=self.clearTextField)
        trackButton.place(x=250, y=290)

    # Функция очистки всего поля с полученными сообщениями
    def clearTextField(self):
        self.textFrame.delete('1.0', END)
