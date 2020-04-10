# !/usr/bin/python
# -*- coding: utf-8 -*-


class Model:
    def setView(self, view):
        self.view = view

    def sayHello(self):
        print ("Hello, I'm model!")
        self.view.sayHello()
