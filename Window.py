#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Este módulo contiene la clase que crea la ventana"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI_reactivos_ui import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setupUi(self)


    