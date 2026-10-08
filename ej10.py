class Producto:
    def __init__(self, nombre, precio_unitario):
        self.nombre = nombre
        self.precio_unitario = precio_unitario

    def __str__(self):
        return f"{self.nombre} - {self.precio_unitario:,.0f} Gs."


class Item:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def subtotal(self):
        return self.producto.precio_unitario * self.cantidad

    def __str__(self):
        return (
            f"{self.producto.nombre} x {self.cantidad} = "
            f"{self.subtotal():,.0f} Gs."
        )


class Carrito:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)

    def calcular_total(self):
        total = 0
        for item in self.items:
            total += item.subtotal()
        return total

    def mostrar_detalle(self):
        print("Detalle del carrito:")
        for item in self.items:
            print(f"- {item}")
        print(f"Total a pagar: {self.calcular_total():,.0f} Gs.")

    def __str__(self):
        return f"Carrito con {len(self.items)} item(s)"


arroz = Producto("Arroz", 8500)
aceite = Producto("Aceite", 12500)
jabon = Producto("Jabon", 6000)

carrito = Carrito()
carrito.agregar_item(Item(arroz, 2))
carrito.agregar_item(Item(aceite, 1))
carrito.agregar_item(Item(jabon, 3))

print(carrito)
carrito.mostrar_detalle()
