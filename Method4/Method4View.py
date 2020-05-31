# !/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import ProgressBar
import time


class Method_4_View(tk.Toplevel):
    def __init__(self, root, controller):
        super().__init__(root)
        self.main_root = root
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.maxsize(930, 720)
        self.minsize(930, 720)
        self.geometry('+300+300')
        self.grab_set()
        self.focus_set()
        self.title = 'Метод 4'

        # Configuring main label
        mainLabel = tk.Label(self, text='Измерение входных токов и разности входных токов ОУ', font='Regular')
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

        # 2 Установка устройств коммутации 1 и 2 в положение 2
        set1Label = tk.Label(self, text='2. Установите устройства коммутации S1 и S2 в положение 2')
        set1Label.place(x=5, y=140)
        self.set1Button = tk.Button(self, text='Установить', width=10, state=tk.DISABLED,
                                    command=self.set1)
        self.set1Button.place(x=7, y=165)

        # 3 Подать напряжение от источников G1, G2, G3
        voltage1Label = tk.Label(self, text='3. Подать постоянное напряжение от источников G1, G2, G3')
        voltage1Label.place(x=5, y=225)
        self.voltage1Button = tk.Button(self, text='Подать', width=10, state=tk.DISABLED,
                                        command=self.voltage1)
        self.voltage1Button.place(x=7, y=250)

        # 4.1 Переключить устройство выборки и хранения в режим "выборки"
        switch1Label = tk.Label(self, text='4. Переключить устройство выборки и хранения в режим "выборки"')
        switch1Label.place(x=5, y=310)
        self.switch1Button = tk.Button(self, text='Переключить', width=10, state=tk.DISABLED,
                                       command=self.switch1)
        self.switch1Button.place(x=7, y=335)

        # 4.2 Измерение напряжения Ux1
        measure1Label = tk.Label(self, text='5. Измерить напряжение Ux1')
        measure1Label.place(x=5, y=395)
        self.measure1Button = tk.Button(self, text='Измерить', width=10, state=tk.DISABLED,
                                        command=self.measure1)
        self.measure1Button.place(x=7, y=420)

        # 5 Переключить устройство выборки и хранения в режим "хранения"
        switch2Label = tk.Label(self, text='6. Переключить устройство выборки и хранения в режим "хранения"')
        switch2Label.place(x=5, y=480)
        self.switch2Button = tk.Button(self, text='Переключить', width=10, state=tk.DISABLED,
                                       command=self.switch2)
        self.switch2Button.place(x=7, y=505)

        # 6.1 Установка устройства коммутации S1 в положение 1, S2 в положение 2
        set2Label = tk.Label(self, text='7. Установка устройства коммутации S1 в положение 1, S2 в положение 2')
        set2Label.place(x=5, y=565)
        self.set2Button = tk.Button(self, text='Установить', width=10, state=tk.DISABLED,
                                    command=self.set2)
        self.set2Button.place(x=7, y=590)

        # 6.2 Измерение напряжения Ux2
        measure2Label = tk.Label(self, text='8. Измерить напряжение Ux2')
        measure2Label.place(x=5, y=650)
        self.measure2Button = tk.Button(self, text='Измерить', width=10, state=tk.DISABLED,
                                        command=self.measure2)
        self.measure2Button.place(x=7, y=675)

        # 7.1 Установка устройства коммутации S1 в положение 2, S2 в положение 1
        set3Label = tk.Label(self, text='9. Установка устройства коммутации S1 в положение 2, S2 в положение 1')
        set3Label.place(x=500, y=60)
        self.set3Button = tk.Button(self, text='Установить', width=10, state=tk.DISABLED,
                                    command=self.set3)
        self.set3Button.place(x=502, y=85)

        # 7.2 Измерение напряжения Ux3
        measure3Label = tk.Label(self, text='10. Измерить напряжение Ux3')
        measure3Label.place(x=500, y=145)
        self.measure3Button = tk.Button(self, text='Измерить', width=10, state=tk.DISABLED,
                                        command=self.measure3)
        self.measure3Button.place(x=502, y=170)

        # 8.1 Установка устройства коммутации S1 и S2 в положение 1
        set4Label = tk.Label(self, text='11. Установка устройства коммутации S1 и S2 в положение 1')
        set4Label.place(x=500, y=230)
        self.set4Button = tk.Button(self, text='Установить', width=10, state=tk.DISABLED,
                                    command=self.set4)
        self.set4Button.place(x=502, y=255)

        # 8.2 Измерение напряжения Ux2
        measure4Label = tk.Label(self, text='12. Измерить напржение Ux4')
        measure4Label.place(x=500, y=315)
        self.measure4Button = tk.Button(self, text='Измерить', width=10, state=tk.DISABLED,
                                        command=self.measure4)
        self.measure4Button.place(x=502, y=340)

        # 9 Рассчет значений
        calculateLabel = tk.Label(self, text='Нажмите кнопку для рассчета значения')
        calculateLabel.place(x=500, y=400)
        self.calculateButton = tk.Button(self, text='Рассчитать', width=10, state=tk.DISABLED,
                                         command=self.calculate)
        self.calculateButton.place(x=502, y=425)

        # Configuring value part
        value1DescriptionLabel = tk.Label(self, text='Значение входного тока ОУ по инвертирующему входу:')
        value1DescriptionLabel.place(x=500, y=500)
        self.value1Label = tk.Label(self, text='0.00')
        self.value1Label.place(x=845, y=500)

        value2DescriptionLabel = tk.Label(self, text='Значение входного тока ОУ по неинвертирующему входу:')
        value2DescriptionLabel.place(x=500, y=540)
        self.value2Label = tk.Label(self, text='0.00')
        self.value2Label.place(x=845, y=540)

        value3DescriptionLabel = tk.Label(self, text='Значение разности входных токов ОУ:')
        value3DescriptionLabel.place(x=500, y=580)
        self.value3Label = tk.Label(self, text='0.00')
        self.value3Label.place(x=735, y=580)

        value4DescriptionLabel = tk.Label(self, text='Значение среднего входного тока ОУ:')
        value4DescriptionLabel.place(x=500, y=620)
        self.value4Label = tk.Label(self, text='0.00')
        self.value4Label.place(x=735, y=620)

    def temp(self):
        print()

    def turnOnMethod(self):
        self.switchButtonState(self.turnOffButton)
        self.switchButtonState(self.turnOnButton)
        self.switchButtonState(self.set1Button)
        self.onOffLabel['text'] = 'Включено'

        self.controller.turnOnMethod()

    def turnOffMethod(self):
        self.switchButtonState(self.turnOnButton)
        self.switchButtonState(self.turnOffButton)
        self.disableAllMethodButtons()
        self.onOffLabel['text'] = 'Отключено'

        self.controller.turnOffMethod()

    def set1(self):
        self.switchButtonState(self.set1Button)
        self.switchButtonState(self.voltage1Button)

        self.controller.setSigsIn2()

    def voltage1(self):
        self.switchButtonState(self.voltage1Button)
        self.switchButtonState(self.switch1Button)

    def switch1(self):
        self.switchButtonState(self.switch1Button)
        self.switchButtonState(self.measure1Button)

        self.controller.setChoose()

    def measure1(self):
        self.switchButtonState(self.measure1Button)
        self.switchButtonState(self.switch2Button)

    def switch2(self):
        self.switchButtonState(self.switch2Button)
        self.switchButtonState(self.set2Button)

        self.controller.setSave()

    def set2(self):
        self.switchButtonState(self.set2Button)
        self.switchButtonState(self.measure2Button)

        self.controller.setSig1In1()

    def measure2(self):
        self.switchButtonState(self.measure2Button)
        self.switchButtonState(self.set3Button)

    def set3(self):
        self.switchButtonState(self.set3Button)
        self.switchButtonState(self.measure3Button)

        self.controller.changeSigsStates()

    def measure3(self):
        self.switchButtonState(self.measure3Button)
        self.switchButtonState(self.set4Button)

    def set4(self):
        self.switchButtonState(self.set4Button)
        self.switchButtonState(self.measure4Button)

        self.controller.setSigsIn1()

    def measure4(self):
        self.switchButtonState(self.measure4Button)
        self.switchButtonState(self.calculateButton)

    def calculate(self):
        self.switchButtonState(self.calculateButton)

    def disableAllMethodButtons(self):
        self.set1Button['state'] = tk.DISABLED
        self.voltage1Button['state'] = tk.DISABLED
        self.switch1Button['state'] = tk.DISABLED
        self.measure1Button['state'] = tk.DISABLED
        self.switch2Button['state'] = tk.DISABLED
        self.set2Button['state'] = tk.DISABLED
        self.measure2Button['state'] = tk.DISABLED
        self.set3Button['state'] = tk.DISABLED
        self.measure3Button['state'] = tk.DISABLED
        self.set4Button['state'] = tk.DISABLED
        self.measure4Button['state'] = tk.DISABLED
        self.calculateButton['state'] = tk.DISABLED

    def switchButtonState(self, button):
        if button['state'] == tk.NORMAL:
            button['state'] = tk.DISABLED
        else:
            button['state'] = tk.NORMAL
