import pytest
import sys
from mock import patch
import app_code.code as cd
from pathlib import Path
import os
import matplotlib.pyplot as plt

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
    

def test_how_many_print_call(mocker):
    word = 'bien'
    file_dir = os.path.join(BASE_DIR, "ejemplos/data.pkl")
    printer = mocker.patch('builtins.print')
    cd.how_many(word, file_dir)
    assert printer.call_count == 1

def test_how_many_exist_word():
    word = 'bien'
    file_dir = os.path.join(BASE_DIR, "ejemplos/data.pkl")
    assert cd.how_many(word, file_dir) == True

def test_how_many_not_exist_word():
    word = 'adivinanza'
    file_dir = os.path.join(BASE_DIR, "ejemplos/data.pkl")
    assert cd.how_many(word, file_dir) == False

def test_k_frequent_histogram_monkey(monkeypatch):
    k = 5
    frec = {'bien': 5, 'todo': 5, 'por': 5, 'hola': 4, 'estan': 4}
    file_dir = os.path.join(BASE_DIR, "ejemplos/data.pkl")
    mock_show = lambda: None
    monkeypatch.setattr(plt, 'show', mock_show)
    cd.k_frequent_histogram (k,file_dir)
    assert mock_show.show.called()

@pytest.fixture
def mock_show(mocker):
    yield mocker.patch('matplotlib.pyplot.show')
def test_k_frequent_histogram_show (mock_show) :
    k = 5
    frec = {'bien': 5, 'todo': 5, 'por': 5, 'hola': 4, 'estan': 4}
    file_dir = os.path.join(BASE_DIR, "ejemplos/data.pkl")
    cd.k_frequent_histogram (k,file_dir)
    mock_show.assert_called_once()
    


def test_download_book():
    pass

