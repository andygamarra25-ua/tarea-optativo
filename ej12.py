class LineaTelefonica:
    def __init__(self, cliente, gigas_incluidos):
        self.cliente = cliente
        self.gigas_incluidos = gigas_incluidos
        self.gigas_consumidos = 0

    def registrar_consumo(self, gigas):
        if gigas <= 0:
            print("El consumo debe ser mayor a cero.")
            return

        if self.gigas_consumidos + gigas > self.gigas_incluidos:
            print("No se puede registrar todo el consumo: el paquete se agotaria.")
            self.gigas_consumidos = self.gigas_incluidos
        else:
            self.gigas_consumidos += gigas
            print(f"Se registraron {gigas} GB de consumo.")

        if self.gigas_disponibles() == 0:
            print("Aviso: el paquete de datos ya se agoto.")

    def gigas_disponibles(self):
        return self.gigas_incluidos - self.gigas_consumidos

    def __str__(self):
        return (
            f"Linea de {self.cliente}\n"
            f"Plan: {self.gigas_incluidos} GB\n"
            f"Consumido: {self.gigas_consumidos} GB\n"
            f"Disponible: {self.gigas_disponibles()} GB"
        )


linea = LineaTelefonica("Mariana Lopez", 10)
print(linea)
print()

linea.registrar_consumo(3)
print(linea)
print()

linea.registrar_consumo(5)
print(linea)
print()

linea.registrar_consumo(4)
print(linea)
