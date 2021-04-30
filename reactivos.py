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

reactivos = []
productos = []

win.agregar_reactivo.clicked.connect(lambda: agregar_reac(reactivos))

win.agregar_producto.clicked.connect(lambda: agregar_prod(productos))

win.calcular.clicked.connect(lambda: MostrarResultado(reactivos))


def agregar_reac(lista_reactivos):

    lista_reactivos.append(Compuesto(win.reac_formula.text(), int(win.reac_coeficiente.text()), int(win.reac_moles.text())))

    generar_texto(lista_reactivos)

    win.reactivos_ingresados.setText(generar_texto(lista_reactivos))
    
    win.reac_coeficiente.clear()
    win.reac_formula.clear()
    win.reac_moles.clear()


def agregar_prod(lista_productos):

    lista_productos.append(Compuesto(win.prod_formula.text(), int(win.prod_coeficiente.text()), int(win.prod_moles.text())))

    generar_texto(lista_productos)

    win.productos_ingresados.setText(generar_texto(lista_productos))
    
    win.prod_coeficiente.clear()
    win.prod_formula.clear()
    win.prod_moles.clear()


def generar_texto(lista_compuestos):
    texto = ''
    for compuesto in lista_compuestos:
        if compuesto != lista_compuestos[len(lista_compuestos) - 1]:
            texto += f'{compuesto.coeficiente}{compuesto.formula}  +  '
        else:
            texto += f'{compuesto.coeficiente}{compuesto.formula}'

    return texto


def MostrarResultado(compuestos):

    print(len(compuestos))
    

if __name__ == "__main__":
    
    win.show()
    sys.exit(app.exec())
