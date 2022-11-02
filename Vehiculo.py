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

