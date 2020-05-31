# !/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import ProgressBar
import time


class Method_3_View(tk.Toplevel):
    def __init__(self, root, controller):
        super().__init__(root)
        self.main_root = root
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.maxsize(480, 770)
        self.minsize(480, 770)
        self.geometry('+300+300')
        self.grab_set()
        self.focus_set()
        self.title = 'Метод 2'

        # Configuring main label
        mainLabel = tk.Label(self, text='Измерение напряжения и ЭДС смещения нуля ОУ', font='Regular')
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

        # 2 Подача постоянного напряжения источников G1, G2, G3 на ОУ
        voltageLabel = tk.Label(self, text='2. Подайте напряжение на ОУ от источников G1, G2, G3')
        voltageLabel.place(x=5, y=140)
        self.voltageButton = tk.Button(self, text='Подать', width=10, state=tk.DISABLED,
                                       command=self.voltage)
        self.voltageButton.place(x=7, y=165)

        # 3.1 Замкнуть устройства коммутации
        closeLabel = tk.Label(self, text='3. Замкнуть устройства коммутации S1 и S2')
        closeLabel.place(x=5, y=225)
        self.closeButton = tk.Button(self, text='Замкнуть', width=10, state=tk.DISABLED,
                                     command=self.closeSigs)
        self.closeButton.place(x=7, y=250)

        # 3.2 Измерить напряжения Ux1
        measure1Label = tk.Label(self, text='4. Измерить напряжение Ux1')
        measure1Label.place(x=5, y=310)
        self.measure1Button = tk.Button(self, text='Измерить', width=10, state=tk.DISABLED,
                                        command=self.measure1)
        self.measure1Button.place(x=7, y=335)

        # 4.1 Разомкнуть устройства коммутации
        openLabel = tk.Label(self, text='5. Разомкнуть устройства коммутации S1 и S2')
        openLabel.place(x=5, y=395)
        self.openButton = tk.Button(self, text='Разомкнуть', width=10, state=tk.DISABLED,
                                    command=self.openSigs)
        self.openButton.place(x=7, y=420)

        # 4.2 Измерить напряжения Ux2
        measure2Label = tk.Label(self, text='6. Измерить напряжение Ux2')
        measure2Label.place(x=5, y=480)
        self.measure2Button = tk.Button(self, text='Измерить', width=10, state=tk.DISABLED,
                                        command=self.measure2)
        self.measure2Button.place(x=7, y=505)

        # 5 Рассчет значений
        calculateLabel = tk.Label(self, text='Рассчитать значения')
        calculateLabel.place(x=5, y=565)
        self.calculateButton = tk.Button(self, text='Рассчитать', width=10, state=tk.DISABLED,
                                         command=self.calculate)
        self.calculateButton.place(x=7, y=590)

        # Configuring value part
        value1DescriptionLabel = tk.Label(self, text='Значение ЭДС смещения нуля:')
        value1DescriptionLabel.place(x=5, y=650)
        self.value1Label = tk.Label(self, text='0.00')
        self.value1Label.place(x=235, y=650)

        value2DescriptionLabel = tk.Label(self, text='Значение напряжения смещения нуля:')
        value2DescriptionLabel.place(x=5, y=680)
        self.value2Label = tk.Label(self, text='0.00')
        self.value2Label.place(x=235, y=680)

    def temp(self):
        print()

    def turnOnMethod(self):
        self.switchButtonState(self.turnOffButton)
        self.switchButtonState(self.turnOnButton)
        self.switchButtonState(self.voltageButton)
        self.onOffLabel['text'] = 'Включено'

        self.controller.turnOnMethod()

    def turnOffMethod(self):
        self.switchButtonState(self.turnOnButton)
        self.switchButtonState(self.turnOffButton)
        self.disableAllMethodButtons()
        self.onOffLabel['text'] = 'Отключено'

        self.controller.turnOffMethod()

    def voltage(self):
        self.switchButtonState(self.voltageButton)
        self.switchButtonState(self.closeButton)

    def closeSigs(self):
        self.switchButtonState(self.closeButton)
        self.switchButtonState(self.measure1Button)

        self.controller.setSig1Sig2()

    def measure1(self):
        self.switchButtonState(self.measure1Button)
        self.switchButtonState(self.openButton)

    def openSigs(self):
        self.switchButtonState(self.openButton)
        self.switchButtonState(self.measure2Button)

        self.controller.offSig1Sig2()

    def measure2(self):
        self.switchButtonState(self.measure2Button)
        self.switchButtonState(self.calculateButton)

    def calculate(self):
        self.switchButtonState(self.calculateButton)

    def disableAllMethodButtons(self):
        self.voltageButton['state'] = tk.DISABLED
        self.closeButton['state'] = tk.DISABLED
        self.measure1Button['state'] = tk.DISABLED
        self.openButton['state'] = tk.DISABLED
        self.measure2Button['state'] = tk.DISABLED
        self.calculateButton['state'] = tk.DISABLED

    def switchButtonState(self, button):
        if button['state'] == tk.NORMAL:
            button['state'] = tk.DISABLED
        else:
            button['state'] = tk.NORMAL
