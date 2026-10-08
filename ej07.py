class ProductoConStock:
    def __init__(self, nombre, precio_unitario, stock, stock_minimo):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.stock = stock
        self.stock_minimo = stock_minimo

    def ingresar_mercaderia(self, cantidad):
        if cantidad > 0:
            self.stock += cantidad
            print(f"Ingresaron {cantidad} unidades de {self.nombre}.")
        else:
            print("La cantidad debe ser positiva.")
        self.revisar_stock()

    def vender(self, cantidad):
        if cantidad <= 0:
            print("La cantidad vendida debe ser positiva.")
        elif cantidad > self.stock:
            print("No hay stock suficiente para esa venta.")
        else:
            self.stock -= cantidad
            print(f"Se vendieron {cantidad} unidades de {self.nombre}.")
        self.revisar_stock()

    def revisar_stock(self):
        if self.stock < self.stock_minimo:
            print("Alerta: hay que reponer mercaderia.")

    def __str__(self):
        return (
            f"{self.nombre} - Precio: {self.precio_unitario:,.0f} Gs. - "
            f"Stock: {self.stock} unidades - Minimo: {self.stock_minimo}"
        )


producto = ProductoConStock("Yerba mate", 15000, 10, 5)
print(producto)

producto.vender(4)
print(producto)

producto.vender(3)
print(producto)

producto.vender(10)
print(producto)

producto.ingresar_mercaderia(8)
print(producto)
