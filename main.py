from ingeniero_señor import IngenieroSenior

def main():
    senior1 = IngenieroSenior("miguel ardila", 25, 3600, "Desarrolladora", ["Python", "Java", "C++"])
    senior1.agregar_habilidades("Bases de datos")
    senior1.agregar_habilidades("Docker")
    senior1.agregar_habilidades("IA")

    print(senior1.mostrar_info_completa())

main()