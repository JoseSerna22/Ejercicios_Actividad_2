from enum import Enum

UA_KM = 149597870


class TipoPlaneta(Enum):
    # Tipos de planeta
    GASEOSO = 1
    TERRESTRE = 2
    ENANO = 3


class Planeta:
    # Clase planeta

    def __init__(self, nombre=None, satelites=0, masa=0.0, volumen=0.0,
                 diametro=0, distancia_sol=0,
                 tipo: TipoPlaneta = None, observable=False):
        # Constructor
        self.nombre = nombre
        self.satelites = satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo: TipoPlaneta = tipo
        self.observable = observable

    def imprimir(self):
        # Mostrar datos
        print("Nombre:", self.nombre)
        print("Satélites:", self.satelites)
        print("Masa (kg):", self.masa)
        print("Volumen (km3):", self.volumen)
        print("Diámetro (km):", self.diametro)
        print("Distancia al Sol (millones km):", self.distancia_sol)
        print("Tipo:", self.tipo.name if self.tipo else None)
        print("Observable a simple vista:", self.observable)

    def calcular_densidad(self):
        # Masa sobre volumen
        if self.volumen == 0:
            return 0.0
        return self.masa / self.volumen

    def es_exterior(self):
        # Más allá del cinturón
        distancia_km = self.distancia_sol * 1000000
        distancia_ua = distancia_km / UA_KM
        return distancia_ua > 3.4


def main():
    # Crear planetas
    tierra = Planeta("Tierra", 1, 5.972e24, 1.083e12, 12756, 150,
                     TipoPlaneta.TERRESTRE, True)
    jupiter = Planeta("Júpiter", 95, 1.898e27, 1.4313e15, 142984, 778,
                      TipoPlaneta.GASEOSO, True)

    for planeta in (tierra, jupiter):
        planeta.imprimir()
        print("Densidad (kg/km3):", planeta.calcular_densidad())
        print("Es exterior:", planeta.es_exterior())
        print()


main()
