# !/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import Tk

from PowerSupplyController import PowerSupplyController
from PowerSupplyModel import PowerSupplyModel
from PowerSupplyView import PowerSupplyView


def main():
    root = Tk()
    root.maxsize(720, 420)
    root.minsize(720, 420)
    model = PowerSupplyModel()
    controller = PowerSupplyController(model)
    app = PowerSupplyView(root, controller)
    model.setView(app)
    root.mainloop()


if __name__ == '__main__':
    main()