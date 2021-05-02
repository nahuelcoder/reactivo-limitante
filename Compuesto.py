#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Este módulo contiene la clase para crear compuestos"""

class Compuesto:
    
    # Constructor

    def __init__(self, formula, coeficiente, moles):
        self.formula = formula
        self.coeficiente = coeficiente
        self.moles = moles