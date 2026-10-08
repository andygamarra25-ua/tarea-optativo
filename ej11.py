class Estudiante:
    def __init__(self, nombre, nota_minima=60):
        self.nombre = nombre
        self.nota_minima = nota_minima
        self.notas = {}

    def registrar_nota(self, materia, nota):
        if 0 <= nota <= 100:
            self.notas[materia] = nota
        else:
            print("La nota debe estar entre 0 y 100.")

    def calcular_promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas.values()) / len(self.notas)

    def esta_aprobado(self):
        return self.calcular_promedio() >= self.nota_minima

    def __str__(self):
        texto = f"Boletin de {self.nombre}\n"
        for materia, nota in self.notas.items():
            texto += f"- {materia}: {nota}\n"
        texto += f"Promedio: {self.calcular_promedio():.2f}\n"
        texto += "Condicion final: Aprobado" if self.esta_aprobado() else "Condicion final: Reprobado"
        return texto


estudiante = Estudiante("Carlos Duarte")
estudiante.registrar_nota("Python", 85)
estudiante.registrar_nota("Base de datos", 72)
estudiante.registrar_nota("Ingles", 68)

print(estudiante)
