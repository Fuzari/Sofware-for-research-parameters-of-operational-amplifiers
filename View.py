# !/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import BOTH
from ttk import Frame, Button, Label, Combobox


class View(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.equipmentList = Combobox(self, height=30, width=25)

        self.initUI()

    def initUI(self):
        self.parent.title("Software for connecting Rigol measuring equipment")
        self.pack(fill=BOTH, expand=True)

        chooseLabel = Label(self, text='Choose necessary equipment and click the "Connect" button')
        chooseLabel.place(x=10, y=10)

        connectButton = Button(self, text="Connect", command=self.controller.printHello)
        connectButton.place(x=10, y=40)

        self.equipmentList['values'] = ('Power Supply Rigol DP832A',
                                   'Oscilloscope Rigol MSO1104',
                                   'Multimeter Rigol DM3058E')
        self.equipmentList.current(1)
        self.equipmentList.place(x=110, y=40)

    def sayHello(self):
        print ("hello, I'm View!")

