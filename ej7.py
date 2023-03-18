""""
7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). 
El titular será obligatorio y la cantidad es opcional. 
Crear los siguientes métodos para la clase:
● Un constructor, donde los datos pueden estar vacíos.
● Los setters y getters para cada uno de los atributos. 
El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
● mostrar(): Muestra los datos de la cuenta.
● ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad  introducida es negativa, no se hará nada.
● retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
"""


class Cuenta:
    # Atributos de clase
    __titular = ''
    __cantidad = 0

    # Constructor

    def __init__(self):
        self.__titular = ''
        self.__cantidad = 0

    # getter (uso de decoradores)
    # getter y setter para el atributo privado nombre
    # El orden es importante: 1ro el getter y luego el setter

    @property
    def cantidad(self):
        # Obtiene (get) el saldo, protege la información
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular  # Obtiene el nomnre

    @titular.setter
    def titular(self, nombre):  # Repetimos el nombre del método y en el decorador
        self.__titular = nombre  # Es el nombre que le paso como parámetro a la función

    def mostrar(self):
        cadena = "Titular: " + self.titular + \
            " Cantidad: " + str(self.cantidad)
        return cadena

    def ingresar(self, monto):
        if monto > 0:
            self.cantidad= self.cantidad + monto
            print(f'El monto actual es {self.cantidad}')
        else:
            print(f'el monto es menor a cero, no se puede ingresar')
        print('Fin de la transacción')

    def retirar(self, monto):
        self.cantidad= self.cantidad - monto
        print(f'El monto actual es {self.cantidad}')

cliente1 = Cuenta()
print (f'Mostrar cliente1: cliente1.mostrar()')
print(cliente1.mostrar())
cliente1.titular= "Pepe"
print (f'Mostrar cliente1: {cliente1.mostrar()}')
cliente1.ingresar(-10)
print (f'Mostrar cliente1: {cliente1.mostrar()}')
cliente1.ingresar(50)
print (f'Mostrar cliente1: {cliente1.mostrar()}')
cliente1.retirar(20)
print (f'Mostrar cliente1: {cliente1.mostrar()}')
cliente1.retirar(50)
print (f'Mostrar cliente1: {cliente1.mostrar()}')
