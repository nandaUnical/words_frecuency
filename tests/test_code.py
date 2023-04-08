import pytest
import sys
from mock import patch
import app_code.code as cd
from pathlib import Path
import os
import matplotlib.pyplot as plt
import builtins

BASE_DIR = Path(__file__).resolve().parent.parent

#Test correct dict by reading a dir
def test_read_dir_frec ():
    dir_path = os.path.join(BASE_DIR, "ejemplos")
    assert cd.read_dir_frec(dir_path) == {'bien': 5, 'todo': 5, 'por': 5, 'hola': 4, 'estan': 4, 'gracias': 4, 'mundo': 3, 'como': 3, 'aqui': 3, 'preguntar': 3, 'todos': 2, 'muy': 2, 'hoy': 2, 'gente': 2, 'me': 1, 'siento': 1, 'deberiamos': 1, 'celebrarlo': 1, 'hasta': 1, 'pronto': 1, 'la': 1}

#Test correct dict by reading a list of .txt files
def test_read_file_list_frec ():
    dir_path = os.path.join(BASE_DIR, "ejemplos")
    testargs = ["code.py", dir_path + "/texto_1.txt", dir_path + "/texto_2.txt", dir_path + "/texto_3.txt", dir_path + "/texto_4.txt", dir_path + "/texto_5.txt"]
    with patch.object(sys, 'argv', testargs):
        assert cd.read_file_list_frec() == {'bien': 5, 'todo': 5, 'por': 5, 'hola': 4, 'estan': 4, 'gracias': 4, 'mundo': 3, 'como': 3, 'aqui': 3, 'preguntar': 3, 'todos': 2, 'muy': 2, 'hoy': 2, 'gente': 2, 'me': 1, 'siento': 1, 'deberiamos': 1, 'celebrarlo': 1, 'hasta': 1, 'pronto': 1, 'la': 1}

#Test print is called k+1 times in the function
def test_most_frequent_print_call (mocker):
    k = 5
    file_dir = os.path.join(BASE_DIR, "ejemplos/data.pkl")
    printer = mocker.patch('builtins.print')
    cd.most_frequent(k, file_dir)
    assert printer.call_count == k+1

#Test correct most frequent dict
def test_most_frequent_returned_dict ():
    k = 5
    file_dir = os.path.join(BASE_DIR, "ejemplos/data.pkl")
    assert cd.most_frequent(k, file_dir) == {'bien': 5, 'todo': 5, 'por': 5, 'hola': 4, 'estan': 4}
    
#Test that print is called once
def test_how_many_print_call(mocker):
    word = 'bien'
    file_dir = os.path.join(BASE_DIR, "ejemplos/data.pkl")
    printer = mocker.patch('builtins.print')
    cd.how_many(word, file_dir)
    assert printer.call_count == 1

#Test the function with a correct word
def test_how_many_exist_word():
    word = 'bien'
    file_dir = os.path.join(BASE_DIR, "ejemplos/data.pkl")
    assert cd.how_many(word, file_dir) == True

#Test the function with a wrong word
def test_how_many_not_exist_word():
    word = 'adivinanza'
    file_dir = os.path.join(BASE_DIR, "ejemplos/data.pkl")
    assert cd.how_many(word, file_dir) == False

#Test the matplotlib.pyplot.show call with monkeypatch
#def test_k_frequent_histogram_monkey(monkeypatch):
#    k = 5
#    frec = {'bien': 5, 'todo': 5, 'por': 5, 'hola': 4, 'estan': 4}
#    file_dir = os.path.join(BASE_DIR, "ejemplos/data.pkl")
#    mock_show = lambda: None
#    monkeypatch.setattr(plt, 'show', mock_show)
#    cd.k_frequent_histogram (k,file_dir)

#Test the matplotlib.pyplot.show call with a mock fixture
@pytest.fixture
def mock_show(mocker):
    yield mocker.patch('matplotlib.pyplot.show')
def test_k_frequent_histogram_show (mock_show) :
    k = 5
    frec = {'bien': 5, 'todo': 5, 'por': 5, 'hola': 4, 'estan': 4}
    file_dir = os.path.join(BASE_DIR, "ejemplos/data.pkl")
    cd.k_frequent_histogram (k,file_dir)
    mock_show.assert_called_once()

#Test the matplotlib.pyplot.bar call with a mock fixture
@pytest.fixture
def mock_bar(mocker):
    yield mocker.patch('matplotlib.pyplot.bar')
def test_k_frequent_histogram_show (mock_bar) :
    k = 5
    #frec = {'bien': 5, 'todo': 5, 'por': 5, 'hola': 4, 'estan': 4}
    file_dir = os.path.join(BASE_DIR, "ejemplos/data.pkl")
    cd.k_frequent_histogram (k,file_dir)
    mock_bar.assert_called_once_with(['bien','todo','por','hola','estan'], [5,5,5,4,4], 0.50, color='g')
 


def test_download_book_menu(capsys,monkeypatch):
     # inject user input
    monkeypatch.setattr('builtins.input', lambda x: '5')

    # call the menu selection function
    cd.download_book()

    # capture console output
    captured = capsys.readouterr()

    # assert that the output is what we expect
    assert '********YOU HAVE THE FOLLOWING DOWLOAD OPTIONS*********' in captured.out
    assert '1.Download by book ID.' in captured.out
    assert '2.Search by language.' in captured.out
    assert '3.Search words in the titles and authors.' in captured.out
    assert '4.Search by topic.' in captured.out
    assert '5.Exit' in captured.out
    assert '***********************************************************' in captured.out
    #assert 'Choose an option...' in captured.out
    assert '***************LEAVING DOWNLOAD MENU*********************' in captured.out
    #assert '\nPress enter to continue...' in captured.out