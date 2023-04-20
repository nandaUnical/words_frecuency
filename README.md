words_frecuency
-----
This is a terminal-based program to perform some analysis on a collection of *.txt files.

Before using please install the requirements.txt file.

It supports the following features:
+ The program works with either a list of *.txt files or with all the *.txt files in a folder.
    
    `$ python3 ./app_code/code.py ./ejemplos`
    
    `$ python3 ./app_code/code.py ./ejemplos/texto_1.txt  ./ejemplos/texto_2.txt  ./ejemplos/texto_3.txt ./ejemplos/texto_4.txt  ./ejemplos/texto_5.txt`
    

+ It computes word frequencies: how many times a word occurs in a collection of *.txt files.
+ It is not case sensitive and ignores punctuation marks.
+ The frequencies are stored in a file named frec_data.pkl saved in the ./example directory.


+ The application offers an interactive menu and the following queries are supported:

  – Show all words in the text collection and their frequencies. 

  – Show the k most frequent words in the texts.
  
  – Show how many times an input word occurs in the texts.
  
  – Plot an histogram of the frequencies of the k most frequent words in the texts. 
  
  – It provides functionalities to download sample texts from Project Gutenberg’s free e-book collection.
  (Gutendex APIs reference: https://gutendex.com/)
  
+ To download the books another interactive menu is offered with the following options:

  – Download a book from its ID in Project Gutenberg books collection. The results are saved in the downloades_books folder.  The input must be comma separeted:
      
      ` 1 `    or    ` 1,2,3 `   or   ` 1  ,2,  3 ` are equivalents.
     
  – Search books by languague. The input must be comma separeted and with the code of the laguague. You will be able to list the names and ids of books that match your search terms.
  
      ` it `    or    ` it, es `   or   ` it,   es,en ` some examples.
      
  – Search books by keywords in the title and the author fields. The input must be comma separeted:
  
      ` dickens `    or    ` great `   or   ` dickens,great ` some examples.
  
  – Search books by keywords in the topic field. The input must be comma separeted:
  
       ` children `    or    ` life `  some examples.
  
