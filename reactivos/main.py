# -*- coding: utf-8 -*-
# reactivos/main.py

"""Este módulo contiene la aplicación."""

import sys

from PyQt5.QtWidgets import QApplication

from .database import createConnection
from .views import Window


def main():
    """función principal de la aplicación."""

    # Crea la aplicación
    app = QApplication(sys.argv)

    # Conexión con la base de datos
    if not createConnection("contacts.sqlite"):
        sys.exit(1)

    # Crea la ventana principal si la conexión fue exitosa
    win = Window()
    win.show()

    # Ejecuta el ciclo principal
    sys.exit(app.exec())
