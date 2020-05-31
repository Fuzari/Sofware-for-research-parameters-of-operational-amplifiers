# !/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk


class MainView(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.main_root = root
        self.controller = controller
        self.textFrame = tk.Text(self, width=43, height=10)
        self.comPortList = None
        self.initUI()
        self.method1Info = ''
        self.method2Info = ''
        self.method3Info = ''
        self.method4Info = ''
        self.method5Info = ''
        self.method7Info = ''
        self.method10Info = ''
        self.method11_1Info = ''
        self.method11_2Info = ''
        self.method13Info = ''
        self.method17Info = ''

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
        checkAllLabel = tk.Label(self, text='Проверьте подключенные устройства \nперед началом работы',
                                 justify=tk.LEFT)
        checkAllLabel.place(x=380, y=5)

        # Creating a check group of power supply
        checkPowerSupLabel = tk.Label(self, text='Источник питания')
        checkPowerSupLabel.place(x=380, y=45)
        checkPowerSupButton = tk.Button(self, text='Проверить', width=10, command=self.clearTextField)
        checkPowerSupButton.place(x=382, y=70)

        # Creating a check group of multimeter
        checkMultimeterLabel = tk.Label(self, text='Мультиметр')
        checkMultimeterLabel.place(x=515, y=45)
        checkMultimeterButton = tk.Button(self, text='Проверить', width=10, command=self.clearTextField)
        checkMultimeterButton.place(x=517, y=70)
        
        # Creating a check group of Com port
        checkMicrocontrollerLabel = tk.Label(self, text='Активный порт')
        checkMicrocontrollerLabel.place(x=380, y=110)
        self.comPortList = ttk.Combobox(self, values=['COM1', 'COM2', 'COM3'], width=7)
        self.comPortList.current(0)
        self.comPortList.place(x=383, y=130)
        connectComButton = tk.Button(self, text='Подключиться', width=12, command=self.connectComPort)
        connectComButton.place(x=473, y=126)

        # Creating save to file group
        saveToFileLabel = tk.Label(self, text='Для сохранения проведенных\nизмерений нажмите кнопку', justify=tk.LEFT)
        saveToFileLabel.place(x=670, y=5)
        saveToFileButton = tk.Button(self, text="Сохранить", width=10)
        saveToFileButton.place(x=760, y=50)

        # Creating left group of methods
        method1Label = tk.Label(self, text='Метод измерения коэффициента усиления ОУ')
        method1Label.place(x=5, y=250)
        method1Button = tk.Button(self, text='Открыть', width=10, command=self.openMethod1)
        method1Button.place(x=7, y=275)

        method2Label = tk.Label(self, text='Метод измерения максимального выходного напряжения')
        method2Label.place(x=5, y=325)
        method2Button = tk.Button(self, text='Открыть', width=10, command=self.openMethod2)
        method2Button.place(x=7, y=350)

        method3Label = tk.Label(self, text='Метод измерения напряжения и ЭДС смещения нуля ОУ')
        method3Label.place(x=5, y=400)
        method3Button = tk.Button(self, text='Открыть', width=10, command=self.openMethod3)
        method3Button.place(x=7, y=425)

        method4Label = tk.Label(self, justify='left', text='Метод измерения входных токов и разности входных\nтоков ОУ')
        method4Label.place(x=5, y=475)
        method4Button = tk.Button(self, text='Открыть', width=10, command=self.openMethod4)
        method4Button.place(x=7, y=515)

        method5Label = tk.Label(self, justify='left', text='Метод измерения тока потребления и\nпотребляемой мощности ОУ')
        method5Label.place(x=5, y=565)
        method5Button = tk.Button(self, text='Открыть', width=10, command=self.openMethod5)
        method5Button.place(x=7, y=605)

        method7Label = tk.Label(self, justify='left', text='Метод измерения коэффициента влияния нестабильности\nисточников' 
                                                           ' питания на напряжение и ЭДС смещения нуля ОУ')
        method7Label.place(x=5, y=645)
        method7Button = tk.Button(self, text='Открыть', width=10, command=self.openMethod7)
        method7Button.place(x=7, y=685)

        # Creating right group of methods
        method10Label = tk.Label(self, justify='left', text='Метод измерения максимальной скорости и времени нарастания\n'
                                                            'выходного напряжения ОУ')
        method10Label.place(x=380, y=250)
        method10Button = tk.Button(self, text='Открыть', width=10, command=self.openMethod10)
        method10Button.place(x=382, y=290)

        method11_1Label = tk.Label(self, justify='left', text='Метод измерения коэффициента ослабления синфазных входных\n'
                                                              'напряжений ОУ (Метод 1)')
        method11_1Label.place(x=380, y=340)
        method11_1Button = tk.Button(self, text='Открыть', width=10, command=self.openMethod11_1)
        method11_1Button.place(x=382, y=380)

        method11_2Label = tk.Label(self, justify='left', text='Метод измерения коэффициента ослабления синфазных входных\n'
                                                              'напряжений ОУ (Метод 2)')
        method11_2Label.place(x=380, y=430)
        method11_2Button = tk.Button(self, text='Открыть', width=10, command=self.openMethod11_2)
        method11_2Button.place(x=382, y=470)

        method13Label = tk.Label(self, justify='left', text='Метод измерения частоты среза и частоты единичного\n'
                                                            'усиления ОУ')
        method13Label.place(x=380, y=520)
        method13Button = tk.Button(self, text='Открыть', width=10, command=self.openMethod13)
        method13Button.place(x=382, y=570)

        method17Label = tk.Label(self, text='Метод измерения входного и выходного сопротивлений ОУ')
        method17Label.place(x=380, y=620)
        method17Button = tk.Button(self, text='Открыть', width=10, command=self.openMethod17)
        method17Button.place(x=382, y=645)

    # Функция очистки всего поля с полученными сообщениями
    def clearTextField(self):
        self.textFrame.delete('1.0', tk.END)

    # Функции подключения к COM порту
    def connectComPort(self):
        self.controller.connectComPort(self.comPortList.get())

    def comPortIsNotOpened(self):
        self.textFrame.insert('1.0', 'COM порт не открыт.\n')

    def comPortIsOpened(self):
        self.textFrame.insert('1.0', 'COM порт успешно открыт!\n')

    # Функции открытия модулей методов
    def openMethod1(self):
        self.controller.openMethod1(self.main_root)

    def openMethod2(self):
        self.controller.openMethod2(self.main_root)

    def openMethod3(self):
        self.controller.openMethod3(self.main_root)

    def openMethod4(self):
        self.controller.openMethod4(self.main_root)

    def openMethod5(self):
        self.controller.openMethod5(self.main_root)

    def openMethod7(self):
        self.controller.openMethod7(self.main_root)

    def openMethod10(self):
        self.controller.openMethod10(self.main_root)

    def openMethod11_1(self):
        self.controller.openMethod11_1(self.main_root)

    def openMethod11_2(self):
        self.controller.openMethod11_2(self.main_root)

    def openMethod13(self):
        self.controller.openMethod13(self.main_root)

    def openMethod17(self):
        self.controller.openMethod17(self.main_root)



