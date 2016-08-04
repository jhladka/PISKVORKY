#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hra 1D piškvorky podľa materiálov PyLadies Brno


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


def tah(retazec, symbol, policko):
    print retazec[:policko] + '\033[91m' + symbol + '\033[0m' + retazec[policko + 1:]
    return retazec[:policko] + symbol + retazec[policko + 1:]


def tah_hraca(retazec):
    # Vrati herne pole s danym symbolom umiestnenym na poziciu danu hracom
    # odmietne zaporne a prilis velke cislo
    # odmietne tah na obsadene policko
    # hrac hraje s 'x'
    symbol = 'x'
    while True:
        try:
            policko = input(
                'Zadaj číslo políčka (0 až {0}) : '.format(velkost_pola - 1))
            if type(policko) is not int:
                raise TypeError
        except TypeError:
            print ('Musí to byť celé číslo od 0 po {0})!'.format(
                velkost_pola - 1))
        except SyntaxError:
            print ('To nebolo číslo!')
        except NameError:
            print ('To nebolo číslo!')
        else:
            if policko < 0 or policko >= velkost_pola:
                print ('Musíš zadať číslo 0 až {0})!'.format(velkost_pola - 1))
            elif retazec[policko] <> '-':
                print ('Políčko {0} je už obsadené!'.format(policko))
            else:
                break
    return tah(retazec, symbol, policko)


def tah_pocitaca(retazec):
    # Vrati herne pole so zaznamenanym tahom pocitaca
    # pocitac hraje s 'o'
    symbol = 'o'
    print 'Počítač :'
    symboly = (['-oo', 0], ['o-o', 1], ['oo-', 2],
               ['-xx', 0], ['x-x', 1], ['xx-', 2],
               ['--o', 1], ['-o-', 0], ['o--', 1],
               ['-x', 0], ['x-', 1])
    policko = -1
    for s in symboly:
        try:
            policko = retazec.index(s[0])
        except ValueError:
            pass
        else:
            policko += s[1]
            break
    if policko == -1:
        policko = retazec.index('-')
    return tah(retazec, symbol, policko)


def piskvorky1d(N):
    pole = N * '-'
    print pole
    vysledok = '-'
    hrac = 0
    tah = (tah_hraca, tah_pocitaca)
    while vysledok == '-':
        pole = tah[hrac](pole)
        # print pole
        vysledok = vyhodnot(pole)
        hrac = (hrac + 1) % 2
    if vysledok == 'x':
        vypis = 'Gratulujem vyhral si!'
    elif vysledok == 'o':
        vypis = 'Bohužiaľ, počítač bol lepší!'
    else:
        vypis = 'Skončilo to remízou.'
    print vypis

velkost_pola = 20
piskvorky1d(velkost_pola)
# pole = raw_input('Zadaj reťazec s herným poľom:')
