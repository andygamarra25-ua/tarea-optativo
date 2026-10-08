class Habitacion:
    def __init__(self, numero, tipo, tarifa_por_noche):
        self.numero = numero
        self.tipo = tipo
        self.tarifa_por_noche = tarifa_por_noche
        self.ocupada = False

    def ocupar(self):
        if self.ocupada:
            print("La habitacion ya esta ocupada.")
        else:
            self.ocupada = True
            print("La habitacion fue ocupada.")

    def liberar(self):
        if self.ocupada:
            self.ocupada = False
            print("La habitacion fue liberada.")
        else:
            print("La habitacion ya estaba libre.")

    def calcular_estadia(self, noches):
        if noches <= 0:
            return 0
        return self.tarifa_por_noche * noches

    def __str__(self):
        estado = "Ocupada" if self.ocupada else "Libre"
        return (
            f"Habitacion {self.numero}\n"
            f"Tipo: {self.tipo}\n"
            f"Tarifa por noche: {self.tarifa_por_noche:,.0f} Gs.\n"
            f"Estado: {estado}"
        )


habitacion = Habitacion(204, "Doble", 280000)
print(habitacion)
print()

habitacion.ocupar()
print(habitacion)
print()

noches = 3
print(f"Costo por {noches} noches: {habitacion.calcular_estadia(noches):,.0f} Gs.")
print()

habitacion.ocupar()
print()

habitacion.liberar()
print(habitacion)
