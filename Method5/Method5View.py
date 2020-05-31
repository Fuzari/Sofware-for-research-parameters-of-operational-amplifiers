# !/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import ProgressBar
import time


class Method_5_View(tk.Toplevel):
    def __init__(self, root, controller):
        super().__init__(root)
        self.main_root = root
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.maxsize(510, 450)
        self.minsize(510, 450)
        self.geometry('+300+300')
        self.grab_set()
        self.focus_set()
        self.title = 'Метод 5'

        # Configuring main label
        mainLabel = tk.Label(self, text='Измерение тока потребления и потребляемой мощности ОУ', font='Regular')
        mainLabel.place(x=5, y=5)

        # 1 Configuring On/off part of Sch1
        turnLabel = tk.Label(self, text='1. Нажмите нужную кнопку, чтобы включить\отключить режим измерения')
        turnLabel.place(x=5, y=60)
        self.turnOnButton = tk.Button(self, text='Включить', width=10, command=self.turnOnMethod)
        self.turnOnButton.place(x=7, y=85)
        self.turnOffButton = tk.Button(self, text='Отключить', width=10, state=tk.DISABLED, command=self.turnOffMethod)
        self.turnOffButton.place(x=110, y=85)

        stateLabel = tk.Label(self, text='Состояние:')
        stateLabel.place(x=220, y=80)
        self.onOffLabel = tk.Label(self, text='Отключено')
        self.onOffLabel.place(x=290, y=80)

        # 2 Подача постоянного напряжения источника G ОУ
        voltage1Label = tk.Label(self, text='2. Подайте напряжение на ОУ от источника G')
        voltage1Label.place(x=5, y=140)
        self.voltage1Button = tk.Button(self, text='Подать', width=10, state=tk.DISABLED,
                                        command=self.voltage1)
        self.voltage1Button.place(x=7, y=165)

        # 3 Измерение тока
        measure1Label = tk.Label(self, text='3. Измерить ток потребления')
        measure1Label.place(x=5, y=225)
        self.measure1Button = tk.Button(self, text='Измерить', width=10, state=tk.DISABLED,
                                        command=self.measure1)
        self.measure1Button.place(x=7, y=250)

        # 4 Рассчет значения
        calculateLabel = tk.Label(self, text='Нажмите кнопку для рассчета значения')
        calculateLabel.place(x=5, y=310)
        self.calculateButton = tk.Button(self, text='Рассчитать', width=10, state=tk.DISABLED,
                                         command=self.calculate)
        self.calculateButton.place(x=7, y=335)

        # Configuring value part
        value1DescriptionLabel = tk.Label(self, text='Значение коэффициента усиления ОУ:')
        value1DescriptionLabel.place(x=5, y=390)
        self.value1Label = tk.Label(self, text='0.00')
        self.value1Label.place(x=235, y=390)

        value2DescriptionLabel = tk.Label(self, text='Значение коэффициента усиления ОУ:')
        value2DescriptionLabel.place(x=5, y=410)
        self.value2Label = tk.Label(self, text='0.00')
        self.value2Label.place(x=235, y=410)

    def temp(self):
        print()

    def turnOnMethod(self):
        self.switchButtonState(self.turnOffButton)
        self.switchButtonState(self.turnOnButton)
        self.switchButtonState(self.voltage1Button)
        self.onOffLabel['text'] = 'Включено'

        self.controller.turnOnMethod()

    def turnOffMethod(self):
        self.switchButtonState(self.turnOnButton)
        self.switchButtonState(self.turnOffButton)
        self.disableAllMethodButtons()
        self.onOffLabel['text'] = 'Отключено'

        self.controller.turnOffMethod()

    def voltage1(self):
        self.switchButtonState(self.voltage1Button)
        self.switchButtonState(self.measure1Button)

    def measure1(self):
        self.switchButtonState(self.measure1Button)
        self.switchButtonState(self.calculateButton)

    def calculate(self):
        self.switchButtonState(self.calculateButton)

    def disableAllMethodButtons(self):
        self.voltage1Button['state'] = tk.DISABLED
        self.measure1Button['state'] = tk.DISABLED
        self.calculateButton['state'] = tk.DISABLED

    def switchButtonState(self, button):
        if button['state'] == tk.NORMAL:
            button['state'] = tk.DISABLED
        else:
            button['state'] = tk.NORMAL
