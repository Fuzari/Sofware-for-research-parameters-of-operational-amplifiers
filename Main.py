# !/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import Tk
from View import View
from Model import Model
from Controller import Controller

def main():
    root = Tk()
    root.maxsize(450, 200)
    root.minsize(450, 200)
    model = Model()
    controller = Controller(model)
    app = View(root, controller)
    model.setView(app)
    root.mainloop()


if __name__ == '__main__':
    main()