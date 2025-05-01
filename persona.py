class Persona:

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def mostrar_info(self):
        return f"Hola, me llamo {self.__nombre}, mi edad es: {self.__edad} años"

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        self.__edad = nueva_edad

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre