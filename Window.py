#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI_reactivos_ui import Ui_MainWindow
from Compuesto import Compuesto

class Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setupUi(self)

        reactivos = []
        productos = []

        """ print('reactivos lista')
        print(reactivos) """

        self.calcular.clicked.connect(lambda: self.MostrarResultado(reactivos))


    def MostrarResultado(self, compuestos=None):

        if compuestos is None:
            compuestos = []

        compuestos.append(Compuesto(self.reac1Formula.text(), self.reac1Coef.text(), self.reac1Moles.text()))
        texto = compuestos[0].formula
        self.resultado.setText(compuestos[0].formula)
        print(texto)

    