# !/usr/bin/python
# -*- coding: utf-8 -*-

import time
import tkinter as tk
from tkinter import ttk

class ProgressBarView(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.initUI()
        self.showLoading()

    def initUI(self):
        self.maxsize(200, 20)
        self.minsize(200, 20)
        self.geometry('+630+630')
        self.grab_set()
        self.focus_set()
        self.title = 'Загрузка...'

        self.progressBar = ttk.Progressbar(self, orient='horizontal', length=200, mode='determinate')
        self.progressBar.place(x=0, y=0)

    def showLoading(self):
        self.progressBar['maximum'] = 100
        for i in range(41):
            time.sleep(0.05)
            self.progressBar['value'] += i
            self.progressBar.update()
        self.destroy()
