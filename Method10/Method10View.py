# !/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import ProgressBar
import time


class Method_10_View(tk.Toplevel):
    def __init__(self, root, controller):
        super().__init__(root)
        self.main_root = root
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.maxsize(450, 770)
        self.minsize(450, 770)
        self.geometry('+300+300')
        self.grab_set()
        self.focus_set()
        self.title = 'Метод 2'

        # Configuring main label
        mainLabel = tk.Label(self, text='Измерение коэффициента усиления ОУ', font='Regular')
        mainLabel.place(x=5, y=5)

        # 1 Configuring On/off part of Sch1
        turnLabel = tk.Label(self, text='1. Нажмите нужную кнопку, чтобы включить\отключить режим измерения')
        turnLabel.place(x=5, y=60)
        self.turnOnButton = tk.Button(self, text='Включить', width=10)
        self.turnOnButton.place(x=7, y=85)
        self.turnOffButton = tk.Button(self, text='Отключить', width=10, state=tk.DISABLED)
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

        # 4 Перевод устройства DS в режим хранения
        switchLabel = tk.Label(self, text='3. Перевести устройство DS в режим хранения')
        switchLabel.place(x=5, y=225)
        self.switchButton = tk.Button(self, text='Перевести', width=10, state=tk.DISABLED,
                                      command=self.switch)
        self.switchButton.place(x=7, y=250)

        # 5 Подача постоянного напряжения U1
        voltage1Label = tk.Label(self, text='4. Подать постоянное напряжение U1 от источника G3')
        voltage1Label.place(x=5, y=310)
        self.voltage1Button = tk.Button(self, text='Подать', width=10, state=tk.DISABLED,
                                        command=self.voltage1)
        self.voltage1Button.place(x=7, y=335)

        # 6 Измерение напряжения Ux1
        measure1Label = tk.Label(self, text='5. Измерить напржение Ux1')
        measure1Label.place(x=5, y=395)
        self.measure1Button = tk.Button(self, text='Измерить', width=10, state=tk.DISABLED,
                                        command=self.measure1)
        self.measure1Button.place(x=7, y=420)

        # 7 Подача постоянного напряжения U2
        voltage2Label = tk.Label(self, text='6. Подать постоянное напряжение U2 от источника G3')
        voltage2Label.place(x=5, y=480)
        self.voltage2Button = tk.Button(self, text='Подать', width=10, state=tk.DISABLED,
                                        command=self.voltage2)
        self.voltage2Button.place(x=7, y=505)

        # 8 Измерение напряжения Ux2
        measure2Label = tk.Label(self, text='7. Измерить напржение Ux2')
        measure2Label.place(x=5, y=565)
        self.measure2Button = tk.Button(self, text='Измерить', width=10, state=tk.DISABLED,
                                        command=self.measure2)
        self.measure2Button.place(x=7, y=590)

        # 9 Рассчет значения
        calculateLabel = tk.Label(self, text='Нажмите кнопку для рассчета значения')
        calculateLabel.place(x=5, y=650)
        self.calculateButton = tk.Button(self, text='Рассчитать', width=10, state=tk.DISABLED,
                                         command=self.calculateValue)
        self.calculateButton.place(x=7, y=675)

        # Configuring value part
        valueDescriptionLabel = tk.Label(self, text='Значение коэффициента усиления ОУ:')
        valueDescriptionLabel.place(x=5, y=735)
        self.valueLabel = tk.Label(self, text='0.00')
        self.valueLabel.place(x=235, y=735)