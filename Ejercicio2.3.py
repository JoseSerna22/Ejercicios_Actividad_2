from enum import Enum


class Combustible(Enum):
    # Tipos de combustible
    GASOLINA = 1
    BIOETANOL = 2
    DIESEL = 3
    BIODIESEL = 4
    GAS_NATURAL = 5


class TipoAutomovil(Enum):
    # Tipos de automóvil
    CIUDAD = 1
    SUBCOMPACTO = 2
    COMPACTO = 3
    FAMILIAR = 4
    EJECUTIVO = 5
    SUV = 6


class Color(Enum):
    # Colores disponibles
    BLANCO = 1
    NEGRO = 2
    ROJO = 3
    NARANJA = 4
    AMARILLO = 5
    VERDE = 6
    AZUL = 7
    VIOLETA = 8


class Automovil:
    # Clase automóvil

    def __init__(self, marca, modelo, motor,
                 combustible: Combustible, tipo: TipoAutomovil,
                 puertas, asientos, velocidad_maxima,
                 color: Color, velocidad_actual=0):
        # Constructor
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.combustible: Combustible = combustible
        self.tipo: TipoAutomovil = tipo
        self.puertas = puertas
        self.asientos = asientos
        self.velocidad_maxima = velocidad_maxima
        self.color: Color = color
        self.velocidad_actual = velocidad_actual

    # Métodos get
    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_motor(self):
        return self.motor

    def get_combustible(self):
        return self.combustible

    def get_tipo(self):
        return self.tipo

    def get_puertas(self):
        return self.puertas

    def get_asientos(self):
        return self.asientos

    def get_velocidad_maxima(self):
        return self.velocidad_maxima

    def get_color(self):
        return self.color

    def get_velocidad_actual(self):
        return self.velocidad_actual

    # Métodos set
    def set_marca(self, marca):
        self.marca = marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_motor(self, motor):
        self.motor = motor

    def set_combustible(self, combustible):
        self.combustible = combustible

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_puertas(self, puertas):
        self.puertas = puertas

    def set_asientos(self, asientos):
        self.asientos = asientos

    def set_velocidad_maxima(self, velocidad_maxima):
        self.velocidad_maxima = velocidad_maxima

    def set_color(self, color):
        self.color = color

    def set_velocidad_actual(self, velocidad_actual):
        self.velocidad_actual = velocidad_actual

    def acelerar(self, incremento):
        # Subir velocidad
        nueva = self.velocidad_actual + incremento
        if nueva > self.velocidad_maxima:
            print("No se puede superar la velocidad máxima")
        else:
            self.velocidad_actual = nueva

    def desacelerar(self, decremento):
        # Bajar velocidad
        nueva = self.velocidad_actual - decremento
        if nueva < 0:
            print("La velocidad no puede ser negativa")
        else:
            self.velocidad_actual = nueva

    def frenar(self):
        # Velocidad en cero
        self.velocidad_actual = 0

    def calcular_tiempo_llegada(self, distancia):
        # Distancia sobre velocidad
        if self.velocidad_actual == 0:
            print("El automóvil está detenido")
            return 0.0
        return distancia / self.velocidad_actual

    def imprimir(self):
        # Mostrar datos
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Motor (litros):", self.motor)
        print("Combustible:", self.combustible.name)
        print("Tipo:", self.tipo.name)
        print("Puertas:", self.puertas)
        print("Asientos:", self.asientos)
        print("Velocidad máxima (km/h):", self.velocidad_maxima)
        print("Color:", self.color.name)
        print("Velocidad actual (km/h):", self.velocidad_actual)


def main():
    # Crear automóvil
    auto = Automovil("Mazda", 2022, 2.0, Combustible.GASOLINA,
                     TipoAutomovil.COMPACTO, 4, 5, 200, Color.ROJO)
    auto.imprimir()
    print()

    # Velocidad en 100
    auto.set_velocidad_actual(100)
    print("Velocidad actual:", auto.get_velocidad_actual())

    # Aumentar 20
    auto.acelerar(20)
    print("Velocidad actual:", auto.get_velocidad_actual())

    # Reducir 50
    auto.desacelerar(50)
    print("Velocidad actual:", auto.get_velocidad_actual())

    # Frenar
    auto.frenar()
    print("Velocidad actual:", auto.get_velocidad_actual())


main()
