#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hra 1D piškvorky; PyLadies Brno

from ai import tah_pocitaca
from util import tah

def vyhodnot(retazec):
    # Vyhodnoti retazec s hernym polom: vyhra, remiza, ani jedno
    if 'xxx' in retazec:
        return 'x'
    elif 'ooo' in retazec:
        return 'o'
    elif '-' not in retazec:
        return '!'
    else:
        return '-'


def tah_hraca(retazec):
    # Vrati herne pole s danym symbolom umiestnenym na poziciu danu hracom
    # odmietne zaporne a prilis velke cislo
    # odmietne tah na obsadene policko
    # hrac hraje s 'x'
    velkost_pola = len(retazec)
    if velkost_pola == 0:
        raise ValueError('Prázdne herné pole')
    if '-' not in retazec:
        raise ValueError('Plné herné pole')
    symbol = 'x'
    while True:
        try:
            policko = int(raw_input(
                'Zadaj číslo políčka (0 až {0}) : '.format(velkost_pola - 1)))
        except ValueError:
            print ('Musí to byť celé číslo od 0 po {0})!'.format(
                velkost_pola - 1))
        else:
            if policko < 0 or policko >= velkost_pola:
                print ('Musíš zadať číslo 0 až {0})!'.format(velkost_pola - 1))
            elif retazec[policko] <> '-':
                print ('Políčko {0} je už obsadené!'.format(policko))
            else:
                break
    return tah(retazec, symbol, policko)
    

def piskvorky1d(N):
    pole = N * '-'
    print(pole),
    vysledok = '-'
    hrac = 0
    tah = (tah_hraca, tah_pocitaca)
    while vysledok == '-':
        pole = tah[hrac](pole)
        vysledok = vyhodnot(pole)
        hrac = (hrac + 1) % 2
    if vysledok == 'x':
        vypis = 'Gratulujem vyhral si!'
    elif vysledok == 'o':
        vypis = 'Bohužiaľ, počítač bol lepší!'
    else: 
        vypis = 'Skončilo to remízou.'
    print vypis

    
#if __name__ == '__main__':
#    velkost_pola = 20
#    piskvorky1d()
    