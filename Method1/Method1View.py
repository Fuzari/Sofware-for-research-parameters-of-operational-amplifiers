# !/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import ProgressBar
import time


class Method_1_View(tk.Toplevel):
    def __init__(self, root, controller):
        super().__init__(root)
        self.main_root = root
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.maxsize(450, 830)
        self.minsize(450, 830)
        self.geometry('+300+300')
        self.grab_set()
        self.focus_set()
        self.title = 'Метод 1'

        # Configuring main label
        mainLabel = tk.Label(self, text='Измерение коэффициента усиления ОУ', font='Regular')
        mainLabel.place(x=5, y=5)

        # 1 Configuring On/off part of Sch1
        turnLabel = tk.Label(self, text='1. Нажмите нужную кнопку, чтобы включить\отключить режим измерения')
        turnLabel.place(x=5, y=60)
        self.turnOnButton = tk.Button(self, text='Включить', width=10, command=self.turnOnMethod1)
        self.turnOnButton.place(x=7, y=85)
        self.turnOffButton = tk.Button(self, text='Отключить', width=10, state=tk.DISABLED,
                                       command=self.turnOffMethod1)
        self.turnOffButton.place(x=110, y=85)

        stateLabel = tk.Label(self, text='Состояние:')
        stateLabel.place(x=220, y=80)
        self.onOffLabel = tk.Label(self, text='Отключено')
        self.onOffLabel.place(x=290, y=80)

        # 2 Подача постоянного напряжения источников G1, G2, G4 на ОУ
        voltageLabel = tk.Label(self, text='2. Подайте напряжение на ОУ от источников G1, G2, G4')
        voltageLabel.place(x=5, y=140)
        self.voltageButton = tk.Button(self, text='Подать', width=10, state=tk.DISABLED,
                                       command=self.voltage)
        self.voltageButton.place(x=7, y=165)

        # 3 Перевод устройства DS в режим выборки
        switch1Label = tk.Label(self, text='3. Перевести устройство DS в режим выборки')
        switch1Label.place(x=5, y=225)
        self.switch1Button = tk.Button(self, text='Перевести', width=10, state=tk.DISABLED,
                                       command=self.switch1)
        self.switch1Button.place(x=7, y=250)

        # 4 Перевод устройства DS в режим хранения
        switch2Label = tk.Label(self, text='4. Перевести устройство DS в режим хранения')
        switch2Label.place(x=5, y=310)
        self.switch2Button = tk.Button(self, text='Перевести', width=10, state=tk.DISABLED,
                                      command=self.switch2)
        self.switch2Button.place(x=7, y=335)

        # 5 Подача постоянного напряжения U1
        voltage1Label = tk.Label(self, text='5. Подать постоянное напряжение U1 от источника G3')
        voltage1Label.place(x=5, y=395)
        self.voltage1Button = tk.Button(self, text='Подать', width=10, state=tk.DISABLED,
                                        command=self.voltage1)
        self.voltage1Button.place(x=7, y=420)

        # 6 Измерение напряжения Ux1
        measure1Label = tk.Label(self, text='6. Измерить напржение Ux1')
        measure1Label.place(x=5, y=480)
        self.measure1Button = tk.Button(self, text='Измерить', width=10, state=tk.DISABLED,
                                        command=self.measure1)
        self.measure1Button.place(x=7, y=505)

        # 7 Подача постоянного напряжения U2
        voltage2Label = tk.Label(self, text='7. Подать постоянное напряжение U2 от источника G3')
        voltage2Label.place(x=5, y=565)
        self.voltage2Button = tk.Button(self, text='Подать', width=10, state=tk.DISABLED,
                                        command=self.voltage2)
        self.voltage2Button.place(x=7, y=590)

        # 8 Измерение напряжения Ux2
        measure2Label = tk.Label(self, text='8. Измерить напржение Ux2')
        measure2Label.place(x=5, y=650)
        self.measure2Button = tk.Button(self, text='Измерить', width=10, state=tk.DISABLED,
                                        command=self.measure2)
        self.measure2Button.place(x=7, y=675)

        # 9 Рассчет значения
        calculateLabel = tk.Label(self, text='Нажмите кнопку для рассчета значения')
        calculateLabel.place(x=5, y=735)
        self.calculateButton = tk.Button(self, text='Рассчитать', width=10, state=tk.DISABLED,
                                         command=self.calculateValue)
        self.calculateButton.place(x=7, y=760)

        # Configuring value part
        valueDescriptionLabel = tk.Label(self, text='Значение коэффициента усиления ОУ:')
        valueDescriptionLabel.place(x=5, y=800)
        self.valueLabel = tk.Label(self, text='0.00')
        self.valueLabel.place(x=235, y=800)

    def turnOnMethod1(self):
        self.switchButtonState(self.turnOffButton)
        self.switchButtonState(self.turnOnButton)
        self.switchButtonState(self.voltageButton)
        self.onOffLabel['text'] = 'Включено'

        self.controller.turnOnMethod()

    def turnOffMethod1(self):
        self.switchButtonState(self.turnOnButton)
        self.switchButtonState(self.turnOffButton)
        self.disableAllMethodButtons()
        self.onOffLabel['text'] = 'Отключено'

        self.controller.turnOffMethod()

    def voltage(self):
        self.switchButtonState(self.switch1Button)
        self.switchButtonState(self.voltageButton)

    def switch1(self):
        self.switchButtonState(self.switch2Button)
        self.switchButtonState(self.switch1Button)
        self.controller.inUpravlChoose()

    def switch2(self):
        self.switchButtonState(self.voltage1Button)
        self.switchButtonState(self.switch2Button)
        self.controller.inUpravlSave()

    def voltage1(self):
        self.switchButtonState(self.measure1Button)
        self.switchButtonState(self.voltage1Button)

    def measure1(self):
        self.switchButtonState(self.voltage2Button)
        self.switchButtonState(self.measure1Button)

    def voltage2(self):
        self.switchButtonState(self.measure2Button)
        self.switchButtonState(self.voltage2Button)

    def measure2(self):
        self.switchButtonState(self.calculateButton)
        self.switchButtonState(self.measure2Button)

    def calculateValue(self):
        ProgressBar.ProgressBarView(self.main_root)
        time.sleep(0.05)
        self.valueLabel['text'] = '3.43'

    def switchButtonState(self, button):
        if button['state'] == tk.NORMAL:
            button['state'] = tk.DISABLED
        else:
            button['state'] = tk.NORMAL

    def disableAllMethodButtons(self):
        self.voltageButton['state'] = tk.DISABLED
        self.switch1Button['state'] = tk.DISABLED
        self.switch2Button['state'] = tk.DISABLED
        self.voltage1Button['state'] = tk.DISABLED
        self.measure1Button['state'] = tk.DISABLED
        self.voltage2Button['state'] = tk.DISABLED
        self.measure2Button['state'] = tk.DISABLED
        self.calculateButton['state'] = tk.DISABLED

