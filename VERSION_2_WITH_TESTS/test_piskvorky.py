# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 12:57:06 2016
"""

import pytest
from mock import patch
import piskvorky

def test_vyhodnot():
    assert piskvorky.vyhodnot('ooxxxooxoxox') == 'x'
    assert piskvorky.vyhodnot('oooxxooxoxox') == 'o'
    assert piskvorky.vyhodnot('ooxoxooxoxox') == '!'
    assert piskvorky.vyhodnot('oo-xxooxoxox') == '-'
    assert piskvorky.vyhodnot('oooooooooooo') == 'o'
    

def test_tah():
    assert piskvorky.tah('-------', 'x', 5) == '-----x-'
    assert piskvorky.tah('-------', 'x', 0) == 'x------'

    
def test_tah_pocitaca():
    assert piskvorky.tah_pocitaca('xo-ox') == ('xooox')
    with pytest.raises(ValueError) as excinfo:
        piskvorky.tah_pocitaca('xoxox')
    assert excinfo.value.message == 'Plné herné pole' 
    with pytest.raises(ValueError) as excinfo:
        piskvorky.tah_pocitaca('')
    assert excinfo.value.message == 'Prázdne herné pole'
   

def test_tah_hraca():
    with patch('__builtin__.raw_input', return_value='2'):
        assert piskvorky.tah_hraca('ox---o') == 'oxx--o' 
    with pytest.raises(ValueError) as excinfo:
        piskvorky.tah_hraca('xoxox')
    assert excinfo.value.message == 'Plné herné pole' 
    with pytest.raises(ValueError) as excinfo:
        piskvorky.tah_hraca('')
    assert excinfo.value.message == 'Prázdne herné pole'