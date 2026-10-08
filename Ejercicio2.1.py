class Persona:
    # Clase persona

    def __init__(self, nombre, apellido, documento, anio_nacimiento):
        # Constructor
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.anio_nacimiento = anio_nacimiento

    def imprimir(self):
        # Mostrar datos
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Documento:", self.documento)
        print("Año de nacimiento:", self.anio_nacimiento)
        print()


def main():
    # Crear personas
    persona1 = Persona("Carlos", "Gómez", "1017234567", 1999)
    persona2 = Persona("María", "Rojas", "1037654321", 2001)

    # Mostrar valores
    persona1.imprimir()
    persona2.imprimir()


main()
