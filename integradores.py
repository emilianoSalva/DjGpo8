"""
EJERCICIOS INTEGRADORES
"""


# 1. Escribir una función que calcule el máximo común divisor entre dos números.
"""
El máximo común divisor (mcd) de dos o más números enteros es el mayor número entero que es divisor común de ellos. Por ejemplo, el mcd de 24 y 36 es 12, ya que 12 es el mayor número entero que divide exactamente a ambos números.
La fórmula de Euclides es un algoritmo para encontrar el mcd de dos números enteros. La fórmula establece que el mcd de dos números a y b es igual al mcd de b y el resto de la división de a entre b. Esta fórmula se puede aplicar repetidamente hasta que el resto de la división sea cero, momento en el cual el último divisor no nulo será el mcd buscado.
Por ejemplo, para encontrar el mcd de 24 y 36 utilizando la fórmula de Euclides, se realiza lo siguiente:

Dividimos 36 entre 24 y obtenemos un cociente de 1 y un resto de 12.
El mcd de 24 y 36 es igual al mcd de 24 y 12.
Dividimos 24 entre 12 y obtenemos un cociente de 2 y un resto de 0.
El último divisor no nulo es 12, por lo que el mcd de 24 y 36 es 12.
"""

def mcd(a, b):
    """
    Función que calcula el máximo comun divisor entre 2 números enteros
    """
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a

print(mcd(15, 5))
print(mcd(24, 32))


# 2. Escribir una función que calcule el mínimo común múltiplo entre dos números
"""
Para encontrar el mcm de dos números enteros, podemos utilizar el hecho de que el producto de dos números enteros es igual al producto de su mcd y su mcm. Es decir:
a x b = mcd(a,b) x mcm(a,b)
Por lo tanto, podemos encontrar el mcm de dos números enteros a y b dividiendo su producto por su mcd. Por ejemplo, para encontrar el mcm de 6 y 8 utilizando este método, se realiza lo siguiente:

El mcd de 6 y 8 es 2.
El producto de 6 y 8 es 48.
El mcm de 6 y 8 es igual a 48 dividido por 2, es decir, 24.
"""

def mcm_x_euc(a, b):
    """
    Función que calcula el mcm conociendo el MCD entre 2 números enteros por el método de Euclides
    """
    mcd = mcd(a, b)
    mcm = (a * b) // mcd
    return mcm

print(mcm_x_euc(16, 5))
print(mcm_x_euc(7, 22))

def mcm_x_enu(a, b):
    """
    Función que calcula el mínimo común múltiplo entre 2 números enteros utilizando el método de enumeración de múltiplos. Este método implica enumerar los múltiplos de ambos números hasta encontrar el primer múltiplo común, que será el mínimo común múltiplo. Es importante tener en cuenta que este método puede ser ineficiente para números muy grandes, ya que implica la enumeración de múltiplos.
    """
    i = max(a, b)

    while True:
        if i % a == 0 and i % b == 0:
            return i
        i += 1

print(mcm_x_enu(16,5))
print(mcm_x_enu(7, 22))


# 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

def contar_palabras(cadena):
    # Dividimos la cadena en palabras y las almacenamos en una lista
    palabras = cadena.split()
    # Creamos un diccionario para almacenar la frecuencia de cada palabra
    frecuencia = {}
    # Recorremos cada palabra de la lista
    for palabra in palabras:
        # Si la palabra ya se encuentra en el diccionario, incrementamos su frecuencia
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        # Si la palabra no se encuentra en el diccionario, la agregamos con frecuencia 1
        else:
            frecuencia[palabra] = 1
    # Devolvemos el diccionario con la frecuencia de cada palabra
    return frecuencia

print(contar_palabras(input("Ingrese una cadena de caracteres: ")))


# 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.


# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva.


# 6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
#● Un constructor, donde los datos pueden estar vacíos.
#● Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
#● mostrar(): Muestra los datos de la persona.
#● es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.


#7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase:
#● Un constructor, donde los datos pueden estar vacíos.
#● Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
#● mostrar(): Muestra los datos de la cuenta.
#● ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
#● retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.


# 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase:
#● Un constructor.
#● Los setters y getters para el nuevo atributo.
#● En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
#● Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
#● El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
    
    # Setter
    def set_bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion
    
    # Getter
    def get_bonificacion(self):
        return self.__bonificacion
    
    # Métodos
    def es_titular_valido(self, edad):
        return edad >= 18 and edad < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
    
    def mostrar(self):
        print("Cuenta Joven")
        print("Bonificación:", self.__bonificacion, "%")
