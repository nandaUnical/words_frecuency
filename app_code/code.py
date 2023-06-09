import sys
import fileinput
import re
import os
import pickle
import matplotlib.pyplot as plt
import requests
from pathlib import Path
import json

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
    
    for line in fileinput.input(encoding="utf-8"):#iterando linea a linea de los sys.argv
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
    if int(k) > len(frec):
       print ( "There are not "+str(k)+" words in the vocabulary..." )
    res = dict(list(frec.items())[0:int(k)])
    print("\nThe most frequent words in the collection of documents are:")
    for w in res.keys():
        print("word: ", w, "\tfrequency: ", res[w])

    return res

#Mostrar cuantas veces x aparece en el texto
def how_many (word, file_dir):
    #cargar el diccionario guardado en el pkl file
    with open(file_dir, 'rb') as fp:
        frec = pickle.load(fp)

    if word in frec :
        print("This word appears ", frec[word], " times in the collection.")
        return True
    else:
       print("This word does not occur in the document collection.")
       return False

#Histograma de las k palabras mas frecuentes
def k_frequent_histogram (k,file_dir):
    #cargar el diccionario guardado en el pkl file
    with open(file_dir, 'rb') as fp:
        frec = pickle.load(fp)
    #las k palabras mas frecuentes
    frec = dict(list(frec.items())[0:int(k)])

    print("Showing histogram...")

    keys_list = list(frec.keys())
    values_list = list(frec.values())

    plt.bar(keys_list, values_list, 0.50, color='g')
    plt.show()

#Opcion 1 menu download
def download_by_id (ids):
    ids = ids.replace(" ", "")
    t_ids = ids.split(',')
    for id in t_ids:
        if not id.isdigit():
            print('Wrong id, it should be a number, try again...')
            return False
    try:
        res = requests.get('https://gutendex.com/books?ids='+str(ids))
    except:
        print("Error: Unable to connect to the Project Gutenberg website.")
    else:            
        res = json.loads(res.text)
        temp = res["results"]
        BASE_DIR = Path(__file__).resolve().parent.parent
        for i in temp :
            url = i["formats"]["application/epub+zip"]
            t = requests.get(str(url), allow_redirects=True)
            temp_path = f"downloaded_books/book_id_{str(i['id'])}.epub"
            dir_path = os.path.join(BASE_DIR, temp_path)
            open(dir_path, 'wb').write(t.content)
        print("The books have been downloaded. Check the local directory...")
        return res

#Auxiliar function to print books names to console
def print_books (res):
    counter = 0
    list_books = res["results"]
    for i in list_books :
        counter = counter +1
        print ("Book title "+str(counter)+": ", i["title"], "\tID: ", i["id"])
    while str(res["next"]) != "None" :
        res = requests.get(str(res["next"]))
        res = json.loads(res.text)
        list_books = res["results"]
        for i in list_books :
            counter = counter +1
            print ("Book title"+str(counter)+": ", i["title"], "\tID: ", i["id"])

#Opcion 2 menu download
def search_by_lang (lang):
    lang = lang.replace(" ", "")
    res = requests.get('https://gutendex.com/books?languages='+str(lang))
    res = json.loads(res.text)
    print("There are "+str(res["count"])+" books.")
    if res["count"] != 0:
        q = input ("Do you wanna list them?(yes/no)\t")
        if q.lower()=="yes":
            print_books(res)
            return res["count"]
        

#Opcion 3 menu download
def search_in_title (words):
    lang = ""
    words = words.replace(" ", "")
    words = words.split(",")
    for w in words:
        lang += w+"%20"
    res = requests.get('https://gutendex.com/books?search='+lang[:-3])
    res = json.loads(res.text)
    print("There are "+str(res["count"])+" books.")
    if res["count"] != 0:
        q = input ("Do you wanna list them?(yes/no)\t")
        if q.lower()=="yes":
            print_books(res)
            return res["count"]

#opcion 4 menu download
def search_by_topic(words):
    lang = ""
    words = words.replace(" ", "")
    words = words.split(",")
    for w in words:
        lang += w+"%20"
    res = requests.get('https://gutendex.com/books?topic='+lang[:-3])
    res = json.loads(res.text)
    print("There are "+str(res["count"])+" books.")
    if res["count"] != 0:
        q = input ("Do you wanna list them?(yes/no)\t")
        if q.lower()=="yes":
            print_books(res)
            return res["count"]

#Descargar libros de project gutenberg segun varios criterios de busqueda
def download_book ():
    #Menu de opciones de descarga
    exit_menu_value = False
    while exit_menu_value == False:
        print("\n\n********YOU HAVE THE FOLLOWING DOWNLOAD OPTIONS*********")
        print("1.Download by book ID.")
        print("2.Search by language.")
        print("3.Search words in the titles and authors.")
        print("4.Search by topic.")
        print("5.Exit")
        print("***********************************************************")
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
           ids = input('Enter the Project Gutenberg IDs of the books you want to download separated by comma... ')
           download_by_id(ids)                    

        elif option == "2" :
            lang = input("Enter the code of the languages separated by comma in case there are two or more... ")
            search_by_lang(lang)

        elif option == "3" :
            words = input("Enter the words you want to search separated by comma... ")
            search_in_title(words)
       
        elif option == "4":
            words = input("Enter the words you want to search separated by comma... ")
            search_by_topic(words)
      
        elif option == "5":
            exit_menu_value = True
            print("***************LEAVING DOWNLOAD MENU*********************")
            break
        
        input("\nPress enter to continue...")

    

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
        print("1.Show all words frequencies.")
        print("2.Show the k most frequent words.")
        print("3.Show the frequency of a word in the collection.")
        print("4.Plot an histogram for the k most frequents words.")
        print("5.Download a book from Project Gutenberg's free e-book collection.")
        print("6.Exit")
        print("***********************************************")
        option = input("Choose an option...")
        correct = False
        while ( correct == False ):
            if option.isdigit():
                if int(option) < 0 or int(option) > 6 :
                    option = input("Choose a correct option...")
                else:
                    correct = True
            else:
                option = input("Choose a correct option...")

        if option == "1":
            for w in frec.keys():
                print("word: ", w, "\tfrequency: ", frec[w])  
        elif option == "2" :
            most_frequent(k=input("Enter the number of words...\t"),file_dir='..\\ejemplos\\frec_data.pkl')
        elif option == "3" :
            how_many(word=input("Enter a word to search for...\t"),file_dir='..\\ejemplos\\frec_data.pkl')
        elif option == "4" :
            k_frequent_histogram(k=input("Enter the number of words...\t"),file_dir='..\\ejemplos\\frec_data.pkl')
        elif option == "5":
            download_book()
        elif option == "6":
            exit_value = True
            print("*******************BYE BYE*********************")
            break

        input("\nPress enter to continue...")
    

    
    

