class Vehiculo:
    def __init__(self, marca, modelo, anho, precio):
        self.marca = marca
        self.modelo = modelo
        self.anho = anho
        self.precio = precio

    def descripcion_comercial(self):
        return f"{self.marca} {self.modelo} {self.anho} - {self.precio:,.0f} Gs."

    def __str__(self):
        return f"Vehiculo en venta: {self.descripcion_comercial()}"


vehiculo1 = Vehiculo("Toyota", "Corolla", 2020, 95000000)
vehiculo2 = Vehiculo("Kia", "Sportage", 2019, 110000000)

print(vehiculo1)
print(vehiculo2)
