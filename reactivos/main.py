# -*- coding: utf-8 -*-
# reactivos/main.py

"""Este módulo contiene la aplicación."""

import sys

from PyQt5.QtWidgets import QApplication
from .views import Window


def main():
    """función principal de la aplicación."""

    # Crea la aplicación
    app = QApplication(sys.argv)

    # Crea la ventana principal
    win = Window()
    win.show()

    # Ejecuta el ciclo principal
    sys.exit(app.exec())
