class Cancion:
    def __init__(self, titulo, artista, duracion_segundos):
        self.titulo = titulo
        self.artista = artista
        self.duracion_segundos = duracion_segundos

    def __str__(self):
        minutos = self.duracion_segundos // 60
        segundos = self.duracion_segundos % 60
        return f"{self.titulo} - {self.artista} ({minutos}:{segundos:02d})"


class ListaReproduccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def duracion_total(self):
        total = 0
        for cancion in self.canciones:
            total += cancion.duracion_segundos
        return total

    def __str__(self):
        texto = f"Lista: {self.nombre}\n"
        for cancion in self.canciones:
            texto += f"- {cancion}\n"
        total = self.duracion_total()
        minutos = total // 60
        segundos = total % 60
        texto += f"Duracion total: {minutos}:{segundos:02d}"
        return texto


lista = ListaReproduccion("Musica para estudiar")
lista.agregar_cancion(Cancion("Vivir mi vida", "Marc Anthony", 252))
lista.agregar_cancion(Cancion("Color esperanza", "Diego Torres", 260))
lista.agregar_cancion(Cancion("Rayando el sol", "Mana", 248))

print(lista)
