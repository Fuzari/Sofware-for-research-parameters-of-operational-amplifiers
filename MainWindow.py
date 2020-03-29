# !/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import Tk, BOTH
from ttk import Frame, Button, Label, Combobox
import pyvisa


class MainWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.equipmentList = Combobox(self, height=30, width=25)

        self.initUI()

    def initUI(self):
        self.parent.title("Software for connecting Rigol measuring equipment")
        self.pack(fill=BOTH, expand=True)

        chooseLabel = Label(self, text='Choose necessary equipment and click the "Connect" button')
        chooseLabel.place(x=10, y=10)

        connectButton = Button(self, text="Connect", command=self.determineEquipment)
        connectButton.place(x=10, y=40)

        self.equipmentList['values'] = ('Power Supply Rigol DP832A',
                                   'Oscilloscope Rigol MSO1104',
                                   'Multimeter Rigol DM3058E')
        self.equipmentList.current(1)
        self.equipmentList.place(x=110, y=40)

    # Function to determing chosen equipment
    def determineEquipment(self):
        currentEquipmentIndex = self.equipmentList.current()
        if currentEquipmentIndex == 0:
            currentEquipment="Power Supply Rigol DP832A"
        elif currentEquipmentIndex == 1:
            currentEquipment="Oscilloscope Rigol MSO1104"
        else:
            currentEquipment="Multimeter Rigol DM3058E"

        print(currentEquipment)

def connect(equipment):
    rm = pyvisa.ResourceManager()
    print(rm.list_resources())
    my_instrument = rm.open_resource('GPIB0::14::INSTR') # Здесь имя необходмого инструмента из листа
    my_instrument.query("*IDN?")


def main():
    root = Tk()
    root.maxsize(450, 200)
    root.minsize(450, 200)
    app = MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
