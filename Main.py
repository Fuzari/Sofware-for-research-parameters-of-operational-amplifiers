# !/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import Tk

from Controller import Controller
from Model import Model
from PowerSupplyView import PowerSupplyView


def main():
    root = Tk()
    root.maxsize(720, 420)
    root.minsize(720, 420)
    model = Model()
    controller = Controller(model)
    app = PowerSupplyView(root, controller)
    model.setView(app)
    root.mainloop()


if __name__ == '__main__':
    main()