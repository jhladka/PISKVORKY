# -*- coding: utf-8 -*-

import util

def tah_pocitaca(retazec):
    # Vrati herne pole so zaznamenanym tahom pocitaca
    # pocitac hraje s 'o'
    if len(retazec) == 0:
        raise ValueError('Prázdne herné pole')
    if '-' not in retazec:
        raise ValueError('Plné herné pole')
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
    return util.tah(retazec, symbol, policko)