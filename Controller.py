# !/usr/bin/python
# -*- coding: utf-8 -*-


class Controller:
    def __init__(self, model):
        self.model = model

    def printHello(self):
        print ("hello, I'm Controller!")
        self.model.sayHello()
