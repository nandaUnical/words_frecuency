import pytest
import sys
from mock import patch
import app_code.code as cd
from pathlib import Path
import os

BASE_DIR = Path(r'C:\Users\hp\Documents\!Master\Agile\!!Second Apello\!proyecto\words_frecuency').resolve().parent
os.path.join(BASE_DIR, "ejemplos")
#final_path = os.path.join(BASE_DIR, "ejemplos")
#final_path = os.path.join(BASE_DIR, "ejemplos/data.pkl")


#{'bien': 5, 'todo': 5, 'por': 5, 'hola': 4, 'estan': 4, 'gracias': 4, 'mundo': 3, 'como': 3, 'aqui': 3, 'preguntar': 3, 'todos': 2, 'muy': 2, 'hoy': 2, 'gente': 2, 'me': 1, 'siento': 1, 'deberiamos': 1, 'celebrarlo': 1, 'hasta': 1, 'pronto': 1, 'la': 1}

def test_read_dir_frec ():
    dir_path = os.path.join(BASE_DIR, "ejemplos")
    assert cd.read_dir_frec(dir_path) == {'bien': 5, 'todo': 5, 'por': 5, 'hola': 4, 'estan': 4, 'gracias': 4, 'mundo': 3, 'como': 3, 'aqui': 3, 'preguntar': 3, 'todos': 2, 'muy': 2, 'hoy': 2, 'gente': 2, 'me': 1, 'siento': 1, 'deberiamos': 1, 'celebrarlo': 1, 'hasta': 1, 'pronto': 1, 'la': 1}

def test_read_file_list_frec ():
    dir_path = os.path.join(BASE_DIR, "ejemplos")
    testargs = ["code.py", dir_path + "/texto_1.txt", dir_path + "/texto_2.txt", dir_path + "/texto_3.txt", dir_path + "/texto_4.txt", dir_path + "/texto_5.txt"]
    with patch.object(sys, 'argv', testargs):
        assert cd.read_file_list_frec() == {'bien': 5, 'todo': 5, 'por': 5, 'hola': 4, 'estan': 4, 'gracias': 4, 'mundo': 3, 'como': 3, 'aqui': 3, 'preguntar': 3, 'todos': 2, 'muy': 2, 'hoy': 2, 'gente': 2, 'me': 1, 'siento': 1, 'deberiamos': 1, 'celebrarlo': 1, 'hasta': 1, 'pronto': 1, 'la': 1}

def test_most_frequent_print_call (mocker):
    k = 5
    file_dir = os.path.join(BASE_DIR, "ejemplos/data.pkl")
    printer = mocker.patch('builtins.print')
    cd.most_frequent(k, file_dir)
    assert printer.call_count == k+1

def test_most_frequent_returned_dict ():
    k = 5
    file_dir = os.path.join(BASE_DIR, "ejemplos/data.pkl")
    assert cd.most_frequent(k, file_dir) == {'bien': 5, 'todo': 5, 'por': 5, 'hola': 4, 'estan': 4}
    

def test_how_many(mocker):
    word = 'bien'
    file_dir = os.path.join(BASE_DIR, "ejemplos/data.pkl")
    printer = mocker.patch('builtins.print')
    cd.how_many(word, file_dir)
    assert printer.call_count == 1

def test_k_frequent_histogram():
    pass

def test_download_book():
    pass

