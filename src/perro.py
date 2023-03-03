class Perro:
    '''
    Clase que modela a un perro
    '''

    def __init__(self, raza, edad, nombre):
        self.raza = raza
        self.edad = edad
        self.nombre = nombre

    def cumpleanios(self):
        self.edad += 1
        return f"Felicidades {self.nombre}!! Hoy cumples {self.edad} años"