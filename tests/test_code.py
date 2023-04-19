import pytest
import sys
from mock import patch, MagicMock
import app_code.code as cd
from pathlib import Path
import os

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
    file_dir = os.path.join(BASE_DIR, "ejemplos/frec_data.pkl")
    printer = mocker.patch('builtins.print')
    cd.most_frequent(k, file_dir)
    assert printer.call_count == k+1

#Test correct most frequent dict
def test_most_frequent_returned_dict ():
    k = 5
    file_dir = os.path.join(BASE_DIR, "ejemplos/frec_data.pkl")
    assert cd.most_frequent(k, file_dir) == {'bien': 5, 'todo': 5, 'por': 5, 'hola': 4, 'estan': 4}
    
#Test that print is called once
def test_how_many_print_call(mocker):
    word = 'bien'
    file_dir = os.path.join(BASE_DIR, "ejemplos/frec_data.pkl")
    printer = mocker.patch('builtins.print')
    cd.how_many(word, file_dir)
    assert printer.call_count == 1

#Test the function with a correct word
def test_how_many_exist_word():
    word = 'bien'
    file_dir = os.path.join(BASE_DIR, "ejemplos/frec_data.pkl")
    assert cd.how_many(word, file_dir) == True

#Test the function with a wrong word
def test_how_many_not_exist_word():
    word = 'adivinanza'
    file_dir = os.path.join(BASE_DIR, "ejemplos/frec_data.pkl")
    assert cd.how_many(word, file_dir) == False

#Test the matplotlib.pyplot.show call with a mock fixture
@pytest.fixture
def mock_show(mocker):
    yield mocker.patch('matplotlib.pyplot.show')
def test_k_frequent_histogram_show (mock_show) :
    k = 5
    file_dir = os.path.join(BASE_DIR, "ejemplos/frec_data.pkl")
    cd.k_frequent_histogram (k,file_dir)
    mock_show.assert_called_once()

#Test the matplotlib.pyplot.bar call with a mock fixture
@pytest.fixture
def mock_bar(mocker):
    yield mocker.patch('matplotlib.pyplot.bar')
def test_k_frequent_histogram_show (mock_bar) :
    k = 5
    file_dir = os.path.join(BASE_DIR, "ejemplos/frec_data.pkl")
    cd.k_frequent_histogram (k,file_dir)
    mock_bar.assert_called_once_with(['bien','todo','por','hola','estan'], [5,5,5,4,4], 0.50, color='g')
 

#Testing the print in option 5 download menu
def test_download_book_menu(capsys,monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: '5')
    cd.download_book()
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


#Testing we are getting a dictionary from the web page and we get the correct book
def test_download_by_id():
    ids = "1"
    res = cd.download_by_id(ids)
    assert type(res) is dict

    assert res["results"][0]["id"] == 1

#Testing that we get the corrects books when we get multiple ids 
def test_download_by_mult_id():
    ids = "1,2,3"
    res = cd.download_by_id(ids)

    for i in res["results"] :
        assert i["id"] in [1,2,3]

#Test when no listing books
def test_search_by_lang_print_call (mocker, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 'no')
    lang = 'it'
    printer = mocker.patch('builtins.print')
    cd.search_by_lang(lang)
    assert printer.call_count == 1

#Test print_books function
def test_print_book (mocker):
    printer = mocker.patch('builtins.print')
    res = {
        "count": 3,
        "next": None,
        "previous": None,
        "results": [
            {
            "id": 1,
            "title": "The Declaration of Independence of the United States of America",
            "authors": [
                {
                "name": "Jefferson, Thomas",
                "birth_year": 1743,
                "death_year": 1826
                }
            ],
            "translators": [],
            "subjects": [
                "United States -- History -- Revolution, 1775-1783 -- Sources",
                "United States. Declaration of Independence"
            ],
            "bookshelves": [
                "American Revolutionary War",
                "Politics",
                "United States Law"
            ],
            "languages": [
                "en"
            ],
            "copyright": False,
            "media_type": "Text",
            "formats": {
                "application/x-mobipocket-ebook": "https://www.gutenberg.org/ebooks/1.kf8.images",
                "application/epub+zip": "https://www.gutenberg.org/ebooks/1.epub3.images",
                "text/html": "https://www.gutenberg.org/ebooks/1.html.images",
                "image/jpeg": "https://www.gutenberg.org/cache/epub/1/pg1.cover.medium.jpg",
                "text/plain; charset=us-ascii": "https://www.gutenberg.org/files/1/1-0.txt",
                "text/plain": "https://www.gutenberg.org/ebooks/1.txt.utf-8",
                "application/rdf+xml": "https://www.gutenberg.org/ebooks/1.rdf"
            },
            "download_count": 1165
            },
            {
            "id": 2,
            "title": "The United States Bill of Rights: The Ten Original Amendments to the Constitution of the United States",
            "authors": [
                {
                "name": "United States",
                "birth_year": None,
                "death_year": None
                }
            ],
            "translators": [],
            "subjects": [
                "Civil rights -- United States -- Sources",
                "United States. Constitution. 1st-10th Amendments"
            ],
            "bookshelves": [
                "American Revolutionary War",
                "Politics",
                "United States Law"
            ],
            "languages": [
                "en"
            ],
            "copyright": False,
            "media_type": "Text",
            "formats": {
                "application/x-mobipocket-ebook": "https://www.gutenberg.org/ebooks/2.kf8.images",
                "application/epub+zip": "https://www.gutenberg.org/ebooks/2.epub3.images",
                "text/html": "https://www.gutenberg.org/ebooks/2.html.images",
                "image/jpeg": "https://www.gutenberg.org/cache/epub/2/pg2.cover.medium.jpg",
                "text/plain; charset=us-ascii": "https://www.gutenberg.org/files/2/2.txt",
                "text/plain": "https://www.gutenberg.org/ebooks/2.txt.utf-8",
                "application/rdf+xml": "https://www.gutenberg.org/ebooks/2.rdf"
            },
            "download_count": 648
            },
            {
            "id": 3,
            "title": "John F. Kennedy's Inaugural Address",
            "authors": [
                {
                "name": "Kennedy, John F. (John Fitzgerald)",
                "birth_year": 1917,
                "death_year": 1963
                }
            ],
            "translators": [],
            "subjects": [
                "Presidents -- United States -- Inaugural addresses",
                "United States -- Foreign relations -- 1961-1963"
            ],
            "bookshelves": [],
            "languages": [
                "en"
            ],
            "copyright": False,
            "media_type": "Text",
            "formats": {
                "application/x-mobipocket-ebook": "https://www.gutenberg.org/ebooks/3.kf8.images",
                "application/epub+zip": "https://www.gutenberg.org/ebooks/3.epub3.images",
                "text/html": "https://www.gutenberg.org/ebooks/3.html.images",
                "image/jpeg": "https://www.gutenberg.org/cache/epub/3/pg3.cover.medium.jpg",
                "text/plain; charset=us-ascii": "https://www.gutenberg.org/files/3/3.txt",
                "text/plain": "https://www.gutenberg.org/ebooks/3.txt.utf-8",
                "application/rdf+xml": "https://www.gutenberg.org/ebooks/3.rdf"
            },
            "download_count": 206
            }
        ]
    }
    cd.print_books(res)
    assert printer.call_count == res["count"]

    
        