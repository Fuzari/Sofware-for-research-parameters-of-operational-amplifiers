# !/usr/bin/python
# -*- coding: utf-8 -*-

from MainMenu.MainModel import MainModel

class MainController:
    def __init__(self, model):
        self.model = model

    def connectComPort(self, name):
        self.model.connectComPort(name)

    def openMethod1(self, root):
        self.model.openMethod1(root)

    def openMethod2(self, root):
        self.model.openMethod2(root)

    def openMethod3(self, root):
        self.model.openMethod3(root)

    def openMethod4(self, root):
        self.model.openMethod4(root)

    def openMethod5(self, root):
        self.model.openMethod5(root)

    def openMethod7(self, root):
        self.model.openMethod7(root)

    def openMethod10(self, root):
        self.model.openMethod10(root)

    def openMethod11_1(self, root):
        self.model.openMethod11_1(root)

    def openMethod11_2(self, root):
        self.model.openMethod11_2(root)

    def openMethod13(self, root):
        self.model.openMethod13(root)

    def openMethod17(self, root):
        self.model.openMethod17(root)


