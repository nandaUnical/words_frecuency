import pytest
import app_code.code as cd


#1{'bien': 5, 'todo': 5, 'por': 5, 'hola': 4, 'estan': 4, 'gracias': 4, 'mundo': 3, 'como': 3, 'aqui': 3, 'preguntar': 3, 'todos': 2, 'muy': 2, 'hoy': 2, 'gente': 2, 'me': 1, 'siento': 1, 'deberiamos': 1, 'celebrarlo': 1, 'hasta': 1, 'pronto': 1, 'la': 1}

#2{'bien': 3, 'hola': 2, 'mundo': 2, 'como': 2, 'estan': 2, 'muy': 2, 'hoy': 2, 'todo': 2, 'por': 2, 'todos': 1, 'me': 1, 'siento': 1, 'deberiamos': 1, 'celebrarlo': 1, 'hasta': 1, 'pronto': 1, 'aqui': 1, 'gracias': 1, 'preguntar': 1}

def test_read_dir_frec ():
    dir_path = '../ejemplos/'
    assert cd.read_dir_frec(dir_path) == {'bien': 5, 'todo': 5, 'por': 5, 'hola': 4, 'estan': 4, 'gracias': 4, 'mundo': 3, 'como': 3, 'aqui': 3, 'preguntar': 3, 'todos': 2, 'muy': 2, 'hoy': 2, 'gente': 2, 'me': 1, 'siento': 1, 'deberiamos': 1, 'celebrarlo': 1, 'hasta': 1, 'pronto': 1, 'la': 1}

#def test_read_file_list_frec ():
#    assert cd.read_file_list_frec() == {'bien': 3, 'hola': 2, 'mundo': 2, 'como': 2, 'estan': 2, 'muy': 2, 'hoy': 2, 'todo': 2, 'por': 2, 'todos': 1, 'me': 1, 'siento': 1, 'deberiamos': 1, 'celebrarlo': 1, 'hasta': 1, 'pronto': 1, 'aqui': 1, 'gracias': 1, 'preguntar': 1}

