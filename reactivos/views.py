# -*- coding: utf-8 -*-

"""Este módulo contiene la interfaz para manejar la tabla de reactivos."""

from PyQt5.QtWidgets import (
    QAbstractItemView,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)


class Window(QMainWindow):
    """Ventana principal."""

    def __init__(self, parent=None):
        """Inicializador."""
        super().__init__(parent)
        self.setWindowTitle("Calculadora de reactivo limitante")
        self.resize(700, 350)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.setupUI()

    def setupUI(self):
        """Configuración de la ventana principal."""
        # Crea el widget de la tabla
        self.table = QTableView()
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        # Crea los botones
        self.addButton1 = QPushButton("Agregar ecuación")
        self.addButton2 = QPushButton("Agregar elemento químico")
        self.deleteButton = QPushButton("Borrar")
        self.clearAllButton = QPushButton("Limpiar")
        # Lay out the GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton1)
        layout.addWidget(self.addButton2)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)
