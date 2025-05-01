from persona import Persona

class Empleado(Persona):

    def __init__(self, nombre, edad, salario, cargo):
        super().__init__(nombre, edad)
        self.__salario = salario
        self.__cargo = cargo

    @property
    def salario(self):
        return self.__salario

    @property
    def cargo(self):
        return self.__cargo

    @salario.setter
    def salario(self, nuevo_salario):
        self.__salario = nuevo_salario

    @cargo.setter
    def cargo(self, nuevo_cargo):
        self.__cargo = nuevo_cargo

    def mostrar_info(self):
        return f"{super().mostrar_info()} y trabajo como {self.__cargo}"