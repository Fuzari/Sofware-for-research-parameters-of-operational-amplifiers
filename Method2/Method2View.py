# !/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import ProgressBar
import time


class Method_2_View(tk.Toplevel):
    def __init__(self, root, controller):
        super().__init__(root)
        self.main_root = root
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.maxsize(520, 680)
        self.minsize(520, 680)
        self.geometry('+300+300')
        self.grab_set()
        self.focus_set()
        self.title = 'Метод 2'

        # Configuring main label
        mainLabel = tk.Label(self, text='Измерение максимального выходного напряжения ОУ', font='Regular')
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

        # 2 Подача постоянного напряжения источников G2, G3 на ОУ
        voltageLabel = tk.Label(self, text='2. Подайте напряжение на ОУ от источников G2, G3')
        voltageLabel.place(x=5, y=140)
        self.voltageButton = tk.Button(self, text='Подать', width=10, state=tk.DISABLED,
                                       command=self.sendVoltage)
        self.voltageButton.place(x=7, y=165)

        # 3 Подача постоянного напряжения источника G1 на ОУ
        voltage1Label = tk.Label(self, text='3. Подайте напряжение на ОУ от источника G1')
        voltage1Label.place(x=5, y=225)
        self.voltage1Button = tk.Button(self, text='Подать', width=10, state=tk.DISABLED,
                                        command=self.sendVoltage1)
        self.voltage1Button.place(x=7, y=250)

        # 4.1 Перевод устройства коммутации в положение 1
        set1Label = tk.Label(self, text='4. Перевести устройство коммутации в положение 1')
        set1Label.place(x=5, y=310)
        self.set1Button = tk.Button(self, text='Перевести', width=10, state=tk.DISABLED,
                                    command=self.set1)
        self.set1Button.place(x=7, y=335)

        # 4.2 Измерение напряжения  Uвых,max
        measure1Label = tk.Label(self, text='5. Измереить напряжение Uвых,max')
        measure1Label.place(x=5, y=395)
        self.measure1Button = tk.Button(self, text='Измерить', width=10, state=tk.DISABLED,
                                        command=self.measure1)
        self.measure1Button.place(x=7, y=420)

        # 4.3 Перевод устройства коммутации в положение 2
        set2Label = tk.Label(self, text='6. Перевести устройство коммутации в положение 2')
        set2Label.place(x=5, y=480)
        self.set2Button = tk.Button(self, text='Перевести', width=10, state=tk.DISABLED,
                                    command=self.set2)
        self.set2Button.place(x=7, y=505)

        # 4.4 Измерение напряжения  Uвых,max
        measure2Label = tk.Label(self, text='7. Измереить напряжение Uвых,max')
        measure2Label.place(x=5, y=565)
        self.measure2Button = tk.Button(self, text='Измерить', width=10, state=tk.DISABLED,
                                        command=self.measure2)
        self.measure2Button.place(x=7, y=590)

        # Configuring value part
        valueDescriptionLabel = tk.Label(self, text='Значение максимального выходного напряжения ОУ (1):')
        valueDescriptionLabel.place(x=5, y=640)
        self.valueLabel = tk.Label(self, text='0.00')
        self.valueLabel.place(x=345, y=640)

        valueDescriptionLabel = tk.Label(self, text='Значение максимального выходного напряжения ОУ (2):')
        valueDescriptionLabel.place(x=5, y=660)
        self.valueLabel = tk.Label(self, text='0.00')
        self.valueLabel.place(x=345, y=660)

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

    def sendVoltage(self):
        self.switchButtonState(self.voltage1Button)
        self.switchButtonState(self.voltageButton)

    def sendVoltage1(self):
        self.switchButtonState(self.set1Button)
        self.switchButtonState(self.voltage1Button)

    def set1(self):
        self.switchButtonState(self.measure1Button)
        self.switchButtonState(self.set1Button)

        self.controller.setSig1()

    def measure1(self):
        self.switchButtonState(self.measure1Button)
        self.switchButtonState(self.set2Button)

    def set2(self):
        self.switchButtonState(self.measure2Button)
        self.switchButtonState(self.set2Button)

        self.controller.setSig2()

    def measure2(self):
        self.switchButtonState(self.measure2Button)

    def switchButtonState(self, button):
        if button['state'] == tk.NORMAL:
            button['state'] = tk.DISABLED
        else:
            button['state'] = tk.NORMAL

    def disableAllMethodButtons(self):
        self.voltageButton['state'] = tk.DISABLED
        self.voltage1Button['state'] = tk.DISABLED
        self.set1Button['state'] = tk.DISABLED
        self.measure1Button['state'] = tk.DISABLED
        self.set2Button['state'] = tk.DISABLED
        self.measure2Button['state'] = tk.DISABLED
