# -*- coding: utf-8 -*-

def tah(retazec, symbol, policko):
    print retazec[:policko] + '\033[91m' + symbol + '\033[0m' + retazec[policko + 1:]#, '\r'
    return retazec[:policko] + symbol + retazec[policko + 1:]