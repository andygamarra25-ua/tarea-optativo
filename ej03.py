class Empleado:
    def __init__(self, nombre, cargo, salario_mensual):
        self.nombre = nombre
        self.cargo = cargo
        self.salario_mensual = salario_mensual

    def calcular_salario_anual(self):
        return self.salario_mensual * 13

    def __str__(self):
        return (
            f"Empleado: {self.nombre}\n"
            f"Cargo: {self.cargo}\n"
            f"Salario mensual: {self.salario_mensual:,.0f} Gs.\n"
            f"Salario anual con aguinaldo: {self.calcular_salario_anual():,.0f} Gs."
        )


empleado1 = Empleado("Jose Ramirez", "Cajero", 2800000)
empleado2 = Empleado("Laura Benitez", "Supervisora", 4200000)

print(empleado1)
print()
print(empleado2)
