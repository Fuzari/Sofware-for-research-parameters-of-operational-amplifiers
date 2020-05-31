# !/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import ProgressBar
import time


class Method_11_2_View(tk.Toplevel):
    def __init__(self, root, controller):
        super().__init__(root)
        self.main_root = root
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.maxsize(560, 840)
        self.minsize(560, 840)
        self.geometry('+300+100')
        self.grab_set()
        self.focus_set()
        self.title = 'Метод 2'

        # Configuring main label
        mainLabel = tk.Label(self, text='Измерение коэффициента ослабления синфазных входных\nнапряжений ОУ (Метод 2)', font='Regular',
                             justify=tk.LEFT)
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

        # 2 Подача постоянного напряжения источников G2, G3
        voltage1Label = tk.Label(self, text='2. Подайте напряжения от источников G2, G3')
        voltage1Label.place(x=5, y=140)
        self.voltage1Button = tk.Button(self, text='Подать', width=10, state=tk.DISABLED,
                                        command=self.temp)
        self.voltage1Button.place(x=7, y=165)

        # 3.1 Перевод устройства DS в режим выборки
        switch1Label = tk.Label(self, text='3. Перевести устройство DS в режим выборки')
        switch1Label.place(x=5, y=225)
        self.switch1Button = tk.Button(self, text='Перевести', width=10, state=tk.DISABLED,
                                       command=self.temp)
        self.switch1Button.place(x=7, y=250)

        # 3.2 Перевод устройства DS в режим хранения
        switch2Label = tk.Label(self, text='4. Перевести устройство DS в режим хранения')
        switch2Label.place(x=5, y=310)
        self.switch2Button = tk.Button(self, text='Перевести', width=10, state=tk.DISABLED,
                                       command=self.temp)
        self.switch2Button.place(x=7, y=335)

        # 4 Подача постоянного напряжения Uсф,вх1
        voltage2Label = tk.Label(self, text='5. Подать постоянное напряжение Uсф,вх1 от источника G1')
        voltage2Label.place(x=5, y=395)
        self.voltage2Button = tk.Button(self, text='Подать', width=10, state=tk.DISABLED,
                                        command=self.temp)
        self.voltage2Button.place(x=7, y=420)

        # 5 Измерение напряжения Uх1
        measure1Label = tk.Label(self, text='6. Измерить напржение Uх1')
        measure1Label.place(x=5, y=480)
        self.measure1Button = tk.Button(self, text='Измерить', width=10, state=tk.DISABLED,
                                        command=self.temp)
        self.measure1Button.place(x=7, y=505)

        # 6 Подача постоянного напряжения Uсф,вх2
        voltage3Label = tk.Label(self, text='7. Подать постоянное напряжение Uсф,вх2 от источника G1')
        voltage3Label.place(x=5, y=565)
        self.voltage3Button = tk.Button(self, text='Подать', width=10, state=tk.DISABLED,
                                        command=self.temp)
        self.voltage3Button.place(x=7, y=590)

        # 7 Измерение напряжения Uх2
        measure2Label = tk.Label(self, text='9. Измерить напржение Ux2')
        measure2Label.place(x=5, y=650)
        self.measure2Button = tk.Button(self, text='Измерить', width=10, state=tk.DISABLED,
                                        command=self.temp)
        self.measure2Button.place(x=7, y=675)

        # 8 Рассчет значения
        calculateLabel = tk.Label(self, text='Нажмите кнопку для рассчета значения')
        calculateLabel.place(x=5, y=735)
        self.calculateButton = tk.Button(self, text='Рассчитать', width=10, state=tk.DISABLED,
                                         command=self.temp)
        self.calculateButton.place(x=7, y=760)

        # Configuring value part
        valueDescriptionLabel = tk.Label(self, text='Значение коэффициента синфазных входных напряжений ОУ:')
        valueDescriptionLabel.place(x=5, y=810)
        self.valueLabel = tk.Label(self, text='0.00')
        self.valueLabel.place(x=380, y=810)

    def temp(self):
        print()