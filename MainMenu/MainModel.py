# !/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from Method1 import Method1View, Method1Controller, Method1Model
from Method2 import Method2View, Method2Controller, Method2Model
from Method3 import Method3View, Method3Controller, Method3Model
from Method4 import Method4View, Method4Controller, Method4Model
from Method5 import Method5View, Method5Controller, Method5Model
from Method7 import Method7View, Method7Controller, Method7Model
from Method10 import Method10View, Method10Controller, Method10Model
from Method11_1 import Method11_1View, Method11_1Controller, Method11_1Model
from Method11_2 import Method11_2View, Method11_2Controller, Method11_2Model
from Method13 import Method13View, Method13Controller, Method13Model
from Method17 import Method17View, Method17Controller, Method17Model
import SerialPortCore


class MainModel:
    def __init__(self):
        self.view = None
        self.serialPort = None

    def setView(self, view):
        self.view = view

    def connectComPort(self, name):
        self.serialPort = SerialPortCore.checkComPortAvailable(name)
        if self.serialPort:
            self.view.comPortIsOpened()
        else:
            self.view.comPortIsNotOpened()

    def openMethod1(self, root):
        method1Model = Method1Model.Method1Model(port=self.serialPort)
        method1Controller = Method1Controller.Method1Controller(method1Model)
        method1Model.setView(Method1View.Method_1_View(root, method1Controller))

    def openMethod2(self, root):
        method2Model = Method2Model.Method2Model(port=self.serialPort)
        method2Controller = Method2Controller.Method2Controller(method2Model)
        method2Model.setView(Method2View.Method_2_View(root, method2Controller))

    def openMethod3(self, root):
        method3Model = Method3Model.Method3Model(port=self.serialPort)
        method3Controller = Method3Controller.Method3Controller(method3Model)
        method3Model.setView(Method3View.Method_3_View(root, method3Controller))

    def openMethod4(self, root):
        method4Model = Method4Model.Method4Model(port=self.serialPort)
        method4Controller = Method4Controller.Method4Controller(method4Model)
        method4Model.setView(Method4View.Method_4_View(root, method4Controller))

    def openMethod5(self, root):
        method5Model = Method5Model.Method5Model(port=self.serialPort)
        method5Controller = Method5Controller.Method5Controller(method5Model)
        method5Model.setView(Method5View.Method_5_View(root, method5Controller))

    def openMethod7(self, root):
        method7Model = Method7Model.Method7Model(port=self.serialPort)
        method7Controller = Method7Controller.Method7Controller(method7Model)
        method7Model.setView(Method7View.Method_7_View(root, method7Controller))

    def openMethod10(self, root):
        method10Model = Method10Model.Method10Model(port=self.serialPort)
        method10Controller = Method10Controller.Method10Controller(method10Model)
        method10Model.setView(Method10View.Method_10_View(root, method10Controller))

    def openMethod11_1(self, root):
        method11_1Model = Method11_1Model.Method11_1Model(port=self.serialPort)
        method11_1Controller = Method11_1Controller.Method11_1Controller(method11_1Model)
        method11_1Model.setView(Method11_1View.Method_11_1_View(root, method11_1Controller))

    def openMethod11_2(self, root):
        method11_2Model = Method11_2Model.Method11_2Model(port=self.serialPort)
        method11_2Controller = Method11_2Controller.Method11_2Controller(method11_2Model)
        method11_2Model.setView(Method11_2View.Method_11_2_View(root, method11_2Controller))

    def openMethod13(self, root):
        method13Model = Method13Model.Method13Model(port=self.serialPort)
        method13Controller = Method13Controller.Method13Controller(method13Model)
        method13Model.setView(Method13View.Method_13_View(root, method13Controller))

    def openMethod17(self, root):
        method17Model = Method17Model.Method17Model(port=self.serialPort)
        method17Controller = Method17Controller.Method17Controller(method17Model)
        method17Model.setView(Method17View.Method_17_View(root, method17Controller))





