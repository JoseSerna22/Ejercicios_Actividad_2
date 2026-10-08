from enum import Enum


class TipoCuenta(Enum):
    # Tipos de cuenta
    AHORROS = 1
    CORRIENTE = 2


class CuentaBancaria:
    # Clase cuenta

    def __init__(self, nombres, apellidos, numero, tipo: TipoCuenta):
        # Constructor
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero = numero
        self.tipo: TipoCuenta = tipo
        self.saldo = 0.0

    def imprimir(self):
        # Mostrar datos
        print("Nombres:", self.nombres)
        print("Apellidos:", self.apellidos)
        print("Número de cuenta:", self.numero)
        print("Tipo de cuenta:", self.tipo.name)
        print("Saldo:", self.saldo)
        print()

    def consultar_saldo(self):
        # Devolver saldo
        return self.saldo

    def consignar(self, valor):
        # Sumar al saldo
        if valor <= 0:
            print("El valor debe ser positivo")
            return
        self.saldo += valor
        print("Consignación exitosa:", valor)

    def retirar(self, valor):
        # Restar del saldo
        if valor <= 0:
            print("El valor debe ser positivo")
        elif valor > self.saldo:
            print("Fondos insuficientes")
        else:
            self.saldo -= valor
            print("Retiro exitoso:", valor)


def main():
    # Crear cuenta
    cuenta = CuentaBancaria("Ana María", "Pérez López", "123456789",
                            TipoCuenta.AHORROS)
    cuenta.imprimir()

    # Consignar dinero
    cuenta.consignar(500000)
    print("Saldo actual:", cuenta.consultar_saldo())

    # Retiro válido
    cuenta.retirar(200000)
    print("Saldo actual:", cuenta.consultar_saldo())

    # Retiro inválido
    cuenta.retirar(900000)
    print("Saldo actual:", cuenta.consultar_saldo())

    # Estado final
    cuenta.imprimir()


main()
