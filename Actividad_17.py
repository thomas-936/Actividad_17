import tkinter as tk

class Participante:
    def __init__(self, nombre, institucion):
        self.nombre = nombre
        self.institucion = institucion

    def mostrar_info(self):
        return f"{self.nombre} - {self.institucion}"

class BandaEscolar(Participante):
    CATEGORIAS_VALIDAS = ["Primaria", "Básico", "Diversificado"]
    CRITERIOS_VALIDOS = ["ritmo", "uniformidad", "coreografía", "alineación", "puntualidad"]
