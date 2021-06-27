# EJERCICIO EN CLASES

#Funciones para manejo de archivos
#Manejo de archivos


filename ='Miguel.txt'


try:
    with open(filename) as f_obj:
        contents = f_obj.read()
      #  print(contents)
except FileNotFoundError:
    msg = "mm. parece que el archivo "+ filename + "no existe"
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("el archivo contiene "+ filename + " contiene " + str(num_words) , "palabras")
    print("la palabra Dursley se repìte : ",words.count("Dursley"))
    print("la palabra Dursley se Potter : ",words.count("Potter"))
    print("la palabra Dursley se Dudley : ",words.count("Dudley"))







