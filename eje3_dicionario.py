'''Escribir un programa que reciba una cadena de caracteres y devuelva un 
diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).'''


def diccionario():
    
    #solicito al usuario una entrada de texto
    lista = str(input("ingese su texto: "))
    #genera una lista donde cada palabra es un elemento
    lista = (lista.split())
    # itera la lista formando un diccionario donde el key es la palabra y el valor su repetición
    diccionario={i:lista.count(i) for i in lista}
    # imprimo el diccionario
    print(diccionario)
    
diccionario()
    
    



