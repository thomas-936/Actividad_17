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

    def __init__(self, nombre, intitucion, categoria):
        super().__init__(nombre, intitucion)
        self.categoria = None
        self._puntajes = {}
        self.set_categoria(categoria)

    def set_categoria(self, categoria):
        if categoria not in self.CATEGORIAS_VALIDAS:
            raise ValueError("Categoría inválida.")
            self._categoria = categoria

    def registrar_puntajes(self, puntajes):
        for criterio in self.CRITERIOS_VALIDOS:
            if criterio not in puntajes:
                raise ValueError(f"Falta criterio: {criterio}")
            if not (0 <= puntajes[criterio] <= 10):
                raise ValueError(f"Puntaje inválido en {criterio}")
        self._puntajes = puntajes

    def total(self):
        return sum(self._puntajes.values()) if self._puntajes else 0

    def mostrar_info(self):
        info = f"{self.nombre} ({self.institucion}) - {self._categoria}"
        if self._puntajes:
            info += f" | Total: {self.total()}"
        return info
