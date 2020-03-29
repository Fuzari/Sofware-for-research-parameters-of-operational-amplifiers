# !/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import Tk, BOTH
from ttk import Frame, Button, Label, Combobox


class MainWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Software for connecting Rigol measuring equipment")
        self.pack(fill=BOTH, expand=True)

        chooseLabel = Label(self, text='Choose necessary equipment and click the "Connect" button')
        chooseLabel.place(x=10, y=10)

        connectButton = Button(self, text="Connect")
        connectButton.place(x=10, y=40)

        equipmentList = Combobox(self, height=30, width=25)
        equipmentList['values'] = ('Power Supply Rigol DP832A',
                                   'Oscilloscope Rigol MSO1104',
                                   'Multimeter Rigol DM3058E')
        equipmentList.current(1)
        equipmentList.place(x=110, y=40)


def main():
    root = Tk()
    root.maxsize(450, 200)
    root.minsize(450, 200)
    app = MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
