# !/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import*
from MainMenu.MainView import MainView
from MainMenu.MainModel import MainModel
from MainMenu.MainController import MainController

if __name__ == '__main__':
    root = Tk()
    root.title('Программный комплекс для исследования параметров операционных усилителей')
    root.maxsize(760, 720)
    root.minsize(760, 720)
    root.geometry('+400+200')
    mainModel = MainModel()
    mainController = MainController(model=mainModel)
    mainView = MainView(root, controller=mainController)
    mainModel.setView(mainView)
    root.mainloop()