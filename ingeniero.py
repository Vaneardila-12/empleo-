from empledo import Empleado

class ingeniero(Empleado):
    def __init__(self, nombre, edad, salario, cargo, lenguajes):
        super().__init__(nombre, edad, salario, cargo, )
        self.__lenguajes = lenguajes

    @property
    def lenguajes (Self):
        return Self.__lenguajes
    
    @lenguajes.setter
    def lenguajes (self, nuevos__lenguajes):
        self.__lenguajes= nuevos__lenguajes

    def mostrar_info(self):
        return f"{super().mostrar_info()} manejo los lenguajes de {self.__lenguajes}"