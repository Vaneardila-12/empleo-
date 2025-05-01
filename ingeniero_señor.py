from ingeniero import ingeniero
from habilidades import HabilidadTecnica

class IngenieroSenior(ingeniero, HabilidadTecnica):

    def __init__(self, nombre, edad, salario, cargo, lenguajes):
        super().__init__(nombre, edad, salario, cargo, lenguajes)
        HabilidadTecnica.__init__(self)

    def mostrar_info_completa(self):
        info_base = super().mostrar_info()
        habilidades = self.lista_habilidades()
        return f"{info_base}. Habilidades técnicas: {habilidades}"