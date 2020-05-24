# !/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from Method1 import Method1View


class MainView(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.main_root = root
        self.controller = controller
        self.textFrame = tk.Text(self, width=43, height=10)
        self.comPortList = None
        self.initUI()

    def initUI(self):
        # Configuring a frame
        self.pack(fill=tk.BOTH, expand=True)

        # Creating a label to text field
        fieldLabel = tk.Label(self, text='Информационное поле')
        fieldLabel.place(x=5, y=2)

        # Configuring a text field for getting messages from equipment and MC
        self.textFrame.place(x=5, y=25)

        # Configuring a "Clear" button
        clearButton = tk.Button(self, text='Очистить', width=10, command=self.clearTextField)
        clearButton.place(x=5, y=200)

        # Creating a label of checking true working of devices
        checkAllLabel = tk.Label(self, text='Проверьте подключенные устройства перед началом работы')
        checkAllLabel.place(x=380, y=5)

        # Creating a check group of power supply
        checkPowerSupLabel = tk.Label(self, text='Источник питания')
        checkPowerSupLabel.place(x=380, y=35)
        checkPowerSupButton = tk.Button(self, text='Проверить', width=10, command=self.clearTextField)
        checkPowerSupButton.place(x=382, y=60)

        # Creating a check group of multimeter
        checkMultimeterLabel = tk.Label(self, text='Мультиметр')
        checkMultimeterLabel.place(x=520, y=35)
        checkMultimeterButton = tk.Button(self, text='Проверить', width=10, command=self.clearTextField)
        checkMultimeterButton.place(x=522, y=60)
        
        # Creating a check group of Com port
        checkMicrocontrollerLabel = tk.Label(self, text='Активный порт')
        checkMicrocontrollerLabel.place(x=380, y=110)
        self.comPortList = ttk.Combobox(self, values=['COM1', 'COM2'], width=7)
        self.comPortList.current(0)
        self.comPortList.place(x=383, y=130)
        connectComButton = tk.Button(self, text='Подключиться', width=12, command=self.clearTextField)
        connectComButton.place(x=473, y=126)

        # Creating left group of methods
        method1Label = tk.Label(self, text='Метод измерения коэффициента усиления ОУ')
        method1Label.place(x=5, y=250)
        method1Button = tk.Button(self, text='Открыть', width=10, command=self.openMethod1)
        method1Button.place(x=7, y=275)

        method2Label = tk.Label(self, text='Метод измерения максимального выходного напряжения')
        method2Label.place(x=5, y=325)
        method2Button = tk.Button(self, text='Открыть', width=10, command=self.clearTextField)
        method2Button.place(x=7, y=350)

        method3Label = tk.Label(self, text='Метод измерения напряжения и ЭДС смещения нуля ОУ')
        method3Label.place(x=5, y=400)
        method3Button = tk.Button(self, text='Открыть', width=10, command=self.clearTextField)
        method3Button.place(x=7, y=425)

        method4Label = tk.Label(self, justify='left', text='Метод измерения входных токов и разности входных\nтоков ОУ')
        method4Label.place(x=5, y=475)
        method4Button = tk.Button(self, text='Открыть', width=10, command=self.clearTextField)
        method4Button.place(x=7, y=515)

        method5Label = tk.Label(self, justify='left', text='Метод измерения тока потребления и\nпотребляемой мощности ОУ')
        method5Label.place(x=5, y=565)
        method5Button = tk.Button(self, text='Открыть', width=10, command=self.clearTextField)
        method5Button.place(x=7, y=605)

        method7Label = tk.Label(self, justify='left', text='Метод измерения коэффициента влияния нестбильности\nисточников' 
                                                           'питания на напряжение и ЭДС смещения нуля ОУ')
        method7Label.place(x=5, y=645)
        method7Button = tk.Button(self, text='Открыть', width=10, command=self.clearTextField)
        method7Button.place(x=7, y=685)

        # Creating right group of methods
        method10Label = tk.Label(self, justify='left', text='Метод измерения максимальной скорости и времени нарастания\n'
                                                            'выходного напряжения ОУ')
        method10Label.place(x=380, y=250)
        method10Button = tk.Button(self, text='Открыть', width=10, command=self.clearTextField)
        method10Button.place(x=382, y=290)

        method11_1Label = tk.Label(self, justify='left', text='Метод измерения коэффициента ослабления синфазных входных\n'
                                                              'напряжений ОУ')
        method11_1Label.place(x=380, y=340)
        method11_1Button = tk.Button(self, text='Открыть', width=10, command=self.clearTextField)
        method11_1Button.place(x=382, y=380)

        method11_2Label = tk.Label(self, justify='left', text='Метод измерения коэффициента ослабления синфазных входных\n'
                                                              'напряжений ОУ')
        method11_2Label.place(x=380, y=430)
        method11_2Button = tk.Button(self, text='Открыть', width=10, command=self.clearTextField)
        method11_2Button.place(x=382, y=470)

        method13Label = tk.Label(self, justify='left', text='Метод измерения частоты среза и частоты единичного\n'
                                                            'усиления ОУ')
        method13Label.place(x=380, y=520)
        method13Button = tk.Button(self, text='Открыть', width=10, command=self.clearTextField)
        method13Button.place(x=382, y=570)

        method17Label = tk.Label(self, text='Метод измерения входного и выходного сопротивлений ОУ')
        method17Label.place(x=380, y=620)
        method17Button = tk.Button(self, text='Открыть', width=10, command=self.clearTextField)
        method17Button.place(x=382, y=645)

    # Функция очистки всего поля с полученными сообщениями
    def clearTextField(self):
        self.textFrame.delete('1.0', tk.END)

    # Функции открытия модулей методов
    def openMethod1(self):
        Method1View.Method_1_View(root=self.main_root)


