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
        self.voltageEntry = Entry(self, width=10)
        self.amperageEntry = Entry(self, width=10)
        self.limitEntry = Entry(self, width=10)

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
        self.voltageEntry.place(x=120, y=270)

        amperageLabel = Label(self, text='Enter amperage:')
        amperageLabel.place(x=2, y=305)
        self.amperageEntry.place(x=120, y=300)

        limitLabel = Label(self, text='Enter overcurrent\n protection limit:')
        limitLabel.place(x=2, y=335)
        self.limitEntry.place(x=120, y=340)

    # Функция очистки всего поля с полученными сообщениями
    def clearTextField(self):
        self.textFrame.delete('1.0', END)
