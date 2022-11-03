# Asistencia Noviembre ::Dario Walter Carrizo
class Persona: # Esta clase hereda de la clase objet
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        @property           #
        def nombre(self):
            return self._nombre
        @nombre.setter
        def nombre(self, nombre):
            self.nombre = nombre

        @property
        def edad(self):
            return self._edad

        @edad.setter
        def edad(self, edad):
            self._edad = edad

class Empleado(Persona): # esta clase es hija de la clase persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

        @property
        def sueldo(self):
            return

        @sueldo.setter
        def sueldo(self, sueldo):
            self._sueldo

empleado1 = Empleado ('Dario Carrizo', 52, 93000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)
#Tarea: encapsular los atributos y agregar los metodos getter ande setter
#Crear otro objeto, pasar los datos para nombre, edad y sueldo
#Mostrar estos datos, luego modificar y mostrar nuevamente

empleado2 = Empleado ('Mery', 51, 32000)
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)
empleado2.nombre = 'Mery'
empleado2.edad = 51
empleado2.sueldo = 32000
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)

