import sys
import fileinput
import re
import os
import csv

#calcular la frecuencia de las palabras dado un directorio
def read_dir_frec (dir_path):
    frecuency = {}#dicc para las frecuencias
    for fname in os.listdir(dir_path):
        f = os.path.join(dir_path,fname)#path del fichero
        if os.path.isfile(f) and fname.endswith('.txt'):#solo los .txt
            file = open(f,'r')#abrir el fichero
            for line in file :#iterando en cada linea
                l = re.sub(r'[.,"\'-?:!;]', '', line)#eliminando signos de puntuacion
                words = l.lower().split()
                for w in words:#contando cada palabra
                    if w in frecuency:
                        frecuency[w] += 1
                    else:
                        frecuency[w] = 1
    return frecuency

#calcular la frecuencia de las palabras dado una lista de ficheros
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
        frec = read_dir_frec(sys.argv[1])
    else:
        frec = read_file_list_frec()

    #guardar las frecuencias en un .csv
    with open("..\\ejemplos\\frecuency.csv","w",newline="") as fp:
        #create the writer object
        writer = csv.DictWriter(fp, fieldnames=frec.keys())
        #write the header row
        writer.writeheader()
        #write the data rows
        writer.writerow(frec)


    

