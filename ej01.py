class Cliente:
    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self):
        return (
            f"Ficha del cliente\n"
            f"Nombre: {self.nombre}\n"
            f"Cedula: {self.cedula}\n"
            f"Telefono: {self.telefono}"
        )


cliente1 = Cliente("Carlos Duarte", "4.567.890", "0981 222 333")
cliente2 = Cliente("Mariana Lopez", "5.123.456", "0982 444 555")

print(cliente1)
print()
print(cliente2)
