import math


class Circulo:
    # Clase círculo

    def __init__(self, radio):
        # Constructor
        self.radio = radio

    def calcular_area(self):
        # Pi por radio cuadrado
        return math.pi * math.pow(self.radio, 2)

    def calcular_perimetro(self):
        # Circunferencia
        return 2 * math.pi * self.radio


class Rectangulo:
    # Clase rectángulo

    def __init__(self, base, altura):
        # Constructor
        self.base = base
        self.altura = altura

    def calcular_area(self):
        # Base por altura
        return self.base * self.altura

    def calcular_perimetro(self):
        # Suma de lados
        return 2 * (self.base + self.altura)


class Cuadrado:
    # Clase cuadrado

    def __init__(self, lado):
        # Constructor
        self.lado = lado

    def calcular_area(self):
        # Lado al cuadrado
        return math.pow(self.lado, 2)

    def calcular_perimetro(self):
        # Cuatro lados
        return 4 * self.lado


class TrianguloRectangulo:
    # Clase triángulo

    def __init__(self, base, altura):
        # Constructor
        self.base = base
        self.altura = altura

    def calcular_area(self):
        # Base por altura
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self):
        # Teorema de Pitágoras
        return math.sqrt(math.pow(self.base, 2) + math.pow(self.altura, 2))

    def calcular_perimetro(self):
        # Suma de lados
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo(self):
        # Clasificar lados
        a = self.base
        b = self.altura
        c = self.calcular_hipotenusa()
        ab = math.isclose(a, b)
        ac = math.isclose(a, c)
        bc = math.isclose(b, c)
        if ab and ac and bc:
            return "Equilátero"
        if ab or ac or bc:
            return "Isósceles"
        return "Escaleno"


def main():
    # Clase de prueba
    circulo = Circulo(5)
    print("Círculo")
    print("Radio (cm):", circulo.radio)
    print("Área (cm2):", round(circulo.calcular_area(), 2))
    print("Perímetro (cm):", round(circulo.calcular_perimetro(), 2))
    print()

    rectangulo = Rectangulo(8, 4)
    print("Rectángulo")
    print("Base (cm):", rectangulo.base)
    print("Altura (cm):", rectangulo.altura)
    print("Área (cm2):", rectangulo.calcular_area())
    print("Perímetro (cm):", rectangulo.calcular_perimetro())
    print()

    cuadrado = Cuadrado(6)
    print("Cuadrado")
    print("Lado (cm):", cuadrado.lado)
    print("Área (cm2):", cuadrado.calcular_area())
    print("Perímetro (cm):", cuadrado.calcular_perimetro())
    print()

    triangulo = TrianguloRectangulo(3, 4)
    print("Triángulo rectángulo")
    print("Base (cm):", triangulo.base)
    print("Altura (cm):", triangulo.altura)
    print("Área (cm2):", triangulo.calcular_area())
    print("Perímetro (cm):", triangulo.calcular_perimetro())
    print("Hipotenusa (cm):", triangulo.calcular_hipotenusa())
    print("Tipo:", triangulo.determinar_tipo())
    print()

    # Probar isósceles
    triangulo2 = TrianguloRectangulo(5, 5)
    print("Segundo triángulo")
    print("Tipo:", triangulo2.determinar_tipo())


main()
