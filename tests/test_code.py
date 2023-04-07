import pytest
import sys
from mock import patch
import app_code.code as cd


#1{'bien': 5, 'todo': 5, 'por': 5, 'hola': 4, 'estan': 4, 'gracias': 4, 'mundo': 3, 'como': 3, 'aqui': 3, 'preguntar': 3, 'todos': 2, 'muy': 2, 'hoy': 2, 'gente': 2, 'me': 1, 'siento': 1, 'deberiamos': 1, 'celebrarlo': 1, 'hasta': 1, 'pronto': 1, 'la': 1}

def test_read_dir_frec ():
    dir_path = "..\\ejemplos"
    assert cd.read_dir_frec(dir_path) == {'bien': 5, 'todo': 5, 'por': 5, 'hola': 4, 'estan': 4, 'gracias': 4, 'mundo': 3, 'como': 3, 'aqui': 3, 'preguntar': 3, 'todos': 2, 'muy': 2, 'hoy': 2, 'gente': 2, 'me': 1, 'siento': 1, 'deberiamos': 1, 'celebrarlo': 1, 'hasta': 1, 'pronto': 1, 'la': 1}

#def test_read_file_list_frec ():
#    testargs = ["code.py", "../ejemplos/texto_1.txt", "../ejemplos/texto_2.txt", "../ejemplos/texto_3.txt", "../ejemplos/texto_4.txt", "../ejemplos/texto_5.txt"]
#    with patch.object(sys, 'argv', testargs):
#        assert cd.read_file_list_frec() == {'bien': 5, 'todo': 5, 'por': 5, 'hola': 4, 'estan': 4, 'gracias': 4, 'mundo': 3, 'como': 3, 'aqui': 3, 'preguntar': 3, 'todos': 2, 'muy': 2, 'hoy': 2, 'gente': 2, 'me': 1, 'siento': 1, 'deberiamos': 1, 'celebrarlo': 1, 'hasta': 1, 'pronto': 1, 'la': 1}

def test_most_frequent (mocker):
    k = 5
    file_dir = '..\\ejemplos\\data.pkl'
    printer = mocker.patch('builtins.print')
    cd.most_frequent(k, file_dir)
    assert printer.call_count == k+1

def test_how_many(mocker):
    word = 'bien'
    file_dir = '..\\ejemplos\\data.pkl'
    printer = mocker.patch('builtins.print')
    cd.how_many(word, file_dir)
    assert printer.call_count == 1

def test_k_frequent_histogram():
    pass

def test_download_book():
    pass

