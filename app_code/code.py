import sys
import fileinput
import re
import os
import pickle
import matplotlib.pyplot as plt

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
    
    #ordenar dict por valores en orden desc
    frecuency = dict(sorted(frecuency.items(),key=lambda x:x[1],reverse=True))
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

    #ordenar dict por valores en orden desc
    frecuency = dict(sorted(frecuency.items(),key=lambda x:x[1],reverse=True))
    return frecuency

#Mostrar las k palabras mas frecuentes
def most_frequent (k,file_dir):
    #cargar el diccionario guardado en el pkl file
    with open(file_dir, 'rb') as fp:
        frec = pickle.load(fp)

    res = dict(list(frec.items())[0:int(k)])
    print("\nThe most frequent words in the collection of documents are:")
    for w in res.keys():
        print("word: ", w, "\tfrequency: ", res[w])


#Mostrar cuantas veces x aparece en el texto
def how_many (word, file_dir):
    #cargar el diccionario guardado en el pkl file
    with open(file_dir, 'rb') as fp:
        frec = pickle.load(fp)

    print("This word appears ", frec[word], " times in the collection.")

#Histograma de las k palabras mas frecuentes
def k_frequent_histogram (k,file_dir):
    #cargar el diccionario guardado en el pkl file
    with open(file_dir, 'rb') as fp:
        frec = pickle.load(fp)
    #las k palabras mas frecuentes
    frec = dict(list(frec.items())[0:int(k)])

    print("Showing histogram...")

    plt.bar(frec.keys(), frec.values(), 0.50, color='g')
    plt.show()
    

#Programa principal --------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) == 2 :
        frec = read_dir_frec(sys.argv[1])
    else:
        frec = read_file_list_frec()

    #guardar las frecuencias en un .pkl file
    with open('..\\ejemplos\\frec_data.pkl', 'wb') as fp:
        pickle.dump(frec, fp)

    #Menu de opciones
    exit_value = False

    while (exit_value == False):
        print("\n\n********YOU HAVE THE FOLLOWING OPTIONS*********")
        print("1.Show the k most frequent words.")
        print("2.Show the frequency of a word in the collection.")
        print("3.Plot an histogram for the k most frequents words.")
        print("4.Download a book from Project Gutenberg's free e-book collection.")
        print("5.Exit")
        print("***********************************************")
        option = input("Choose an option...")
        correct = False
        while ( correct == False ):
            if option.isdigit():
                if int(option) < 0 or int(option) > 5 :
                    option = input("Choose a correct option...")
                else:
                    correct = True
            else:
                option = input("Choose a correct option...")
            
        if option == "1" :
            most_frequent(k=input("Enter the number of words..."),file_dir='..\\ejemplos\\frec_data.pkl')
        elif option == "2" :
            how_many(word=input("Enter a word to search for..."),file_dir='..\\ejemplos\\frec_data.pkl')
        elif option == "3" :
            k_frequent_histogram(k=input("Enter the number of words..."),file_dir='..\\ejemplos\\frec_data.pkl')
        elif option == "4":
            pass
        elif option == "5":
            exit_value = True
            print("*******************BYE BYE*********************")

        input("\nPress enter to continue...")
    

    
    

