class Producto:
    def __init__(self, nombre, precio_unitario, cantidad_stock):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad_stock = cantidad_stock

    def calcular_valor_total(self):
        return self.precio_unitario * self.cantidad_stock

    def __str__(self):
        return (
            f"Producto: {self.nombre}\n"
            f"Precio unitario: {self.precio_unitario:,.0f} Gs.\n"
            f"Stock: {self.cantidad_stock} unidades\n"
            f"Valor total en stock: {self.calcular_valor_total():,.0f} Gs."
        )


producto1 = Producto("Arroz", 8500, 20)
producto2 = Producto("Aceite", 12500, 12)
producto3 = Producto("Azucar", 7000, 15)

print(producto1)
print()
print(producto2)
print()
print(producto3)
