# Asistencia NOVIEMBRE 2022 ANDRES WINCKLER

"""
    Definir una clase padre llamada Vehiculo y dos clases hijas llamadas
    Auto y bicicleta, las cuales heredan de la clase padre Vehiculo. La clase
    padre deber tener los siguientes atributos y metodos

    Vehiculo(clase padre)
    -Atributos (color, ruedas)
    -Metodos (__init__(color,rueda) y __str__())

    Auto(clase hija de vehiculo)
    -Atributos(velocidad (km/hr))
    -metodods(--init--(color, ruedas, velocidad) y __str__())

    -Bicicleta(clase hija de vehiculo)
    -Atributos(tipo(urbana/montaña/etc.)
    -Metodos(__init__(color, ruedas, tipo) y __str__())

    crear un objeto de cada clase

    """

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color: "+ self.color + " \nruedas: "+ str(self.ruedas)




class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    
    def __str__(self):
        return super().__str__()+ "\nVelocidad(km/h): "+str(self.velocidad)

        

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__()+"\nTipo: "+ self.tipo


# primer objeto clase padre ---> vehiculo
vehiculo = Vehiculo("rojo",4)
print("Objeto clase Vehiculo\n",vehiculo)
#Segundo objeto , el primero de la clase Auto
auto= Auto("Amarillo",6,140)
print("\nobjeto clase Auto\n\n", auto)
#Tercer objeto, primero de la clase Bicicleta
bicicleta = Bicicleta("Negra", 2,"Todo Terreno")
print("\nObjeto clase Bicicleta\n\n",bicicleta)



#Alumno: Martinez Dante Nicolas  -  Asistencia Noviembre

#Herencia Multiple
class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto
    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    def __str__(self):
        return f'FiguraGeometrica [ ancho: {self._ancho}, alto: {self._alto}]'


# asistencia  DARIO CARRIZO
class Persona: # Creamos una clase
#def _init_(self, nombre, apellido, edad): # se lo llama metodo
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        print(type(Persona))

persona1 = persona('dario' , 'carrizo' , "51" ) # necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona( 'mery' , 'maya' , "50" )
print(f'El objeto2 de la clase persona : { persona2.nombre}{persona2.apellid}{persona2.edad}')

persona1 = Persona( 'dario' , 'carrizo' , "51" )
print(f'El objeto1 de la clase persona : { persona1.nombre}{persona1.apellid}{persona1.edad}')

#los atribugtos son las caracteristicas
#los metodos son el comportamiento que a tenen el objeto

#Alumno: Franco Ariel Lara/Asistencia Noviembre
# Tarea crear tres objetos más, utilizando los métodos getter and setter
# para modificar, y mostrar los cambios con el método mostrar detalles
persona2=Persona2('Franco', 'Ariel', 20)
persona2.nombre = 'Fran'
persona2.apellido = 'Lara'
persona2.edad = 21
print(persona2.mostrar_detalles())

persona3 = Persona2('John', 'Connor', 16)
persona3.nombre = 'Johnatan'
persona3.apellido = 'Potato'
persona3.edad = 36
print(persona3.mostrar_detalles())

persona4 =Persona2('Tomas', 'Villalobos', 20)
persona4.nombre = 'Tom'
persona4.apellido = "Lobos"
persona4.edad = 21
print(persona4.mostrar_detalles())

# ASISTENCIA MARISCAL EZEQUIEL

from Color import Color
from FiguraGeometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica, Color):
   def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

   def calcular_area(self):
        return self.alto * self.ancho

   def __str__(self):
        return f'{FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'
    
 # Testeamos
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(5, 'Rojo')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f'Cálculo del área del cuadrado: {cuadrado1.calcular_area()}')

# m.r.o
print(Cuadrado.mro())

print(cuadrado1)

rectangulo1 = Rectangulo(3, 6, 'Verde')
print(f'Cálculo del área del rectángulo: {rectangulo1.calcular_area()}')
print(rectangulo1)


# Abel Pierna
# Asistencia Noviembre 
# Laboratorio 2
# <No_Code/>
class FiguraGeo:
    def __init__(self, ancho, alto):
        self._alto = alto
        self._ancho = ancho
    @property
    def alto(self):
        return self._alto
    @alto.setter
    def alto(self, alto):
        self._alto = alto
    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    def __str__(self):
        return print(f' La Figura Geometrica tiene las siguientes proporciones [ ancho: {self._ancho}, alto: {self._alto}]')
    
    #Jeremias el mas pijon del barrio
    class Persona:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        print(type(Persona))
persona1 = persona('jeremias' , 'riquero' , "18" )
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
persona2 = Persona( 'abel' , 'pierna' , "19" )
print(f'El objeto2 de la clase persona : { persona2.nombre}{persona2.apellid}{persona2.edad}')
persona1 = Persona( 'jeremias' , 'riquero' , "18" )
print(f'El objeto1 de la clase persona : { persona1.nombre}{persona1.apellid}{persona1.edad}')


#ASISTENCIA NOVIEMBRE: Lucas Salinas
persona2 = Persona("Lucas", "Salinas", 19)
persona2.nombre = "Daniel"
persona2.apellido = 'Salinas'
persona2.edad = 19

print(persona2.mostrar_detalles())

persona3 = Persona("Jere", "Riquero", 18)
persona3.nombre = "Jeremias"
persona3.apellido = "Riquero"
persona3.edad = 18

print(persona3.mostrar_detalles())

persona4 = Persona("Abel", "Pierna", 19)
persona4.nombre = "Matias"
persona4.apellido = "Pierna"
persona4.edad = 19

print(persona4.mostrar_detalles())
