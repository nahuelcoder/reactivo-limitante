# -*- coding: utf-8 -*-

"""Este modulo provee la interfaz para realizar las operaciones."""

from PyQt5.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QWidget,
)

class Window(QMainWindow):
    """Ventana principal."""
    def __init__(self, parent=None):
        """Inicializador."""
        super().__init__(parent)
        self.setWindowTitle("Calculadora reactivo limitante")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)