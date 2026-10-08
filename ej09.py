class Turno:
    def __init__(self, paciente, hora):
        self.paciente = paciente
        self.hora = hora
        self.estado = "pendiente"

    def marcar_atendido(self):
        self.estado = "atendido"

    def __str__(self):
        return f"{self.hora} - {self.paciente} ({self.estado})"


class Agenda:
    def __init__(self, fecha):
        self.fecha = fecha
        self.turnos = []

    def agregar_turno(self, turno):
        self.turnos.append(turno)

    def listar_pendientes(self):
        print(f"Turnos pendientes del {self.fecha}:")
        for turno in self.turnos:
            if turno.estado == "pendiente":
                print(f"- {turno}")

    def __str__(self):
        texto = f"Agenda del {self.fecha}\n"
        for turno in self.turnos:
            texto += f"- {turno}\n"
        return texto.strip()


agenda = Agenda("07/10/2026")
turno1 = Turno("Ana Gomez", "08:00")
turno2 = Turno("Pedro Vera", "09:00")
turno3 = Turno("Lucia Torres", "10:00")

agenda.agregar_turno(turno1)
agenda.agregar_turno(turno2)
agenda.agregar_turno(turno3)

print(agenda)
print()

turno1.marcar_atendido()
turno3.marcar_atendido()

agenda.listar_pendientes()
