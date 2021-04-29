#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Este módulo contiene el punto de acceso a la aplicación."""
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from Compuesto import Compuesto
from Window import Window

app = QApplication(sys.argv)
win = Window()


if __name__ == "__main__":
    win = Window()
    win.show()
    sys.exit(app.exec())
