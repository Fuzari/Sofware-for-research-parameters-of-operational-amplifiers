# !/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import ProgressBar
import time


class Method_11_1_View(tk.Toplevel):
    def __init__(self, root, controller):
        super().__init__(root)
        self.main_root = root
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.maxsize(560, 1000)
        self.minsize(560, 1000)
        self.geometry('+300+100')
        self.grab_set()
        self.focus_set()
        self.title = 'Метод 2'

        # Configuring main label
        mainLabel = tk.Label(self, text='Измерение коэффициента ослабления синфазных входных\nнапряжений ОУ (Метод 1)', font='Regular',
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

        # 2 Подача постоянного напряжения источников G1, G2, G4 на ОУ
        voltage1Label = tk.Label(self, text='2. Подайте напряжение на ОУ от источников G1, G2, G4')
        voltage1Label.place(x=5, y=140)
        self.voltage1Button = tk.Button(self, text='Подать', width=10, state=tk.DISABLED,
                                       command=self.temp)
        self.voltage1Button.place(x=7, y=165)

        # 3 Перевод устройства DS в режим выборки
        switch1Label = tk.Label(self, text='3. Перевести устройство DS в режим выборки')
        switch1Label.place(x=5, y=225)
        self.switch1Button = tk.Button(self, text='Перевести', width=10, state=tk.DISABLED,
                                      command=self.temp)
        self.switch1Button.place(x=7, y=250)

        # 4 Перевод устройства DS в режим хранения
        switch2Label = tk.Label(self, text='4. Перевести устройство DS в режим хранения')
        switch2Label.place(x=5, y=310)
        self.switch2Button = tk.Button(self, text='Перевести', width=10, state=tk.DISABLED,
                                       command=self.temp)
        self.switch2Button.place(x=7, y=335)

        # 5 Подача постоянного напряжения Uсф,вх1
        voltage2Label = tk.Label(self, text='5. Подать постоянное напряжение Uсф,вх1 от источника G1')
        voltage2Label.place(x=5, y=395)
        self.voltage2Button = tk.Button(self, text='Подать', width=10, state=tk.DISABLED,
                                        command=self.temp)
        self.voltage2Button.place(x=7, y=420)

        # 6 Измерение напряжения Uсф,вх1
        measure1Label = tk.Label(self, text='6. Измерить напржение Uсф,вх1')
        measure1Label.place(x=5, y=480)
        self.measure1Button = tk.Button(self, text='Измерить', width=10, state=tk.DISABLED,
                                        command=self.temp)
        self.measure1Button.place(x=7, y=505)

        # 7 Измерение напряжения Ux1
        measure2Label = tk.Label(self, text='7. Измерить напржение Ux1')
        measure2Label.place(x=5, y=565)
        self.measure2Button = tk.Button(self, text='Измерить', width=10, state=tk.DISABLED,
                                        command=self.temp)
        self.measure2Button.place(x=7, y=590)

        # 8 Подача постоянного напряжения Uсф,вх2
        voltage3Label = tk.Label(self, text='8. Подать постоянное напряжение Uсф,вх2 от источника G1')
        voltage3Label.place(x=5, y=650)
        self.voltage3Button = tk.Button(self, text='Подать', width=10, state=tk.DISABLED,
                                        command=self.temp)
        self.voltage3Button.place(x=7, y=675)

        # 9 Измерение напряжения Uсф,вх2
        measure3Label = tk.Label(self, text='9. Измерить напржение Uсф,вх2')
        measure3Label.place(x=5, y=735)
        self.measure3Button = tk.Button(self, text='Измерить', width=10, state=tk.DISABLED,
                                        command=self.temp)
        self.measure3Button.place(x=7, y=760)

        # 10 Измерение напряжения Ux2
        measure4Label = tk.Label(self, text='10. Измерить напржение Ux2')
        measure4Label.place(x=5, y=820)
        self.measure4Button = tk.Button(self, text='Измерить', width=10, state=tk.DISABLED,
                                        command=self.temp)
        self.measure4Button.place(x=7, y=845)

        # 11 Рассчет значения
        calculateLabel = tk.Label(self, text='Нажмите кнопку для рассчета значения')
        calculateLabel.place(x=5, y=905)
        self.calculateButton = tk.Button(self, text='Рассчитать', width=10, state=tk.DISABLED,
                                         command=self.temp)
        self.calculateButton.place(x=7, y=930)

        # Configuring value part
        valueDescriptionLabel = tk.Label(self, text='Значение коэффициента синфазных входных напряжений ОУ:')
        valueDescriptionLabel.place(x=5, y=970)
        self.valueLabel = tk.Label(self, text='0.00')
        self.valueLabel.place(x=380, y=970)

    def temp(self):
        print()