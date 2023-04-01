import sys
import fileinput
import re

def read_dir (dir_path):
    pass

def read_file_list_frec ():
    
    frecuency = {} #dict para guardar las frecuencias
    
    for line in fileinput.input(encoding="utf-8"):#iterando sobre los sys.argv
        l = re.sub(r'[.,"\'-?:!;]', '', line)#eliminando signos de puntuacion
        words = l.lower().split()#lower case y separando por palabras
        for w in words:
            if w in frecuency:
                frecuency[w] += 1
            else:
                frecuency[w] = 1

    return frecuency

if __name__ == "__main__":
    if len(sys.argv) == 2 :
        read_dir(sys.argv[1])
    else:
        read_file_list_frec()

