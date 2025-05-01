class HabilidadTecnica:

    def __init__(self):
        self.__habilidades = []

    def agregar_habilidades(self, habilidad):
        self.__habilidades.append(habilidad)

    def lista_habilidades(self):
        return ", ".join(self.__habilidades)