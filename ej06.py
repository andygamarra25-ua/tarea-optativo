class CuentaCorriente:
    def __init__(self, cliente, saldo=0):
        self.cliente = cliente
        self.saldo = saldo

    def acreditar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Se acredito {monto:,.0f} Gs.")
        else:
            print("El monto a acreditar debe ser positivo.")

    def registrar_consumo(self, monto):
        if monto <= 0:
            print("El consumo debe ser mayor a cero.")
        elif monto > self.saldo:
            print("Compra rechazada: saldo insuficiente.")
        else:
            self.saldo -= monto
            print(f"Compra registrada por {monto:,.0f} Gs.")

    def __str__(self):
        return f"Cuenta de {self.cliente} - Saldo actual: {self.saldo:,.0f} Gs."


cuenta = CuentaCorriente("Carlos Duarte")
print(cuenta)

cuenta.acreditar(150000)
print(cuenta)

cuenta.registrar_consumo(45000)
print(cuenta)

cuenta.registrar_consumo(130000)
print(cuenta)

cuenta.acreditar(50000)
print(cuenta)
