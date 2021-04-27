# -*- coding: utf-8 -*-

"""Este módulo contiene la interfaz para manejar la tabla de reactivos."""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QFormLayout,
    QWidget,
    QLabel,
)


class Window(QMainWindow):
    
    """Ventana principal."""

    def __init__(self, parent=None):
        """Inicializador."""
        super().__init__(parent)

        # Propiedades
        self.setWindowTitle("Calculadora de reactivo limitante")
        self.setFixedSize(700, 350)

        # Layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        # Display y botones
        self._crearDisplay()
        self._inputCantReactivos()
        self._crearIngreso()


    def _crearDisplay(self):
        """Crea el display."""
        # Crea el widget del display
        self.display = QLineEdit()

        # Propiedades
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        # comentario random

        # Agrega el display al layout general
        self.generalLayout.addWidget(self.display)


    def _inputCantReactivos(self):
        self.etiqueta = QLabel('Cantidad de reactivos')
        self.etiqueta.setAlignment(Qt.AlignCenter)
        self.cantReactivos = QLineEdit()
        self.generalLayout.addWidget(self.etiqueta)
        self.generalLayout.addWidget(self.cantReactivos)

    def _crearIngreso(self):
        """Crea los botones"""
        self.reactivos = {}
        tam = 3
        botonesLayout = QFormLayout()

        for i in range(tam):
            botonesLayout.addRow(f'Reactivo:{i + 1}', QLineEdit())

        # botonesLayout.addRow('Reactivo:', QLineEdit())
        self.generalLayout.addLayout(botonesLayout)