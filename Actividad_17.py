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

class Concurso:
    def __init__(self, nombre, fecha):
        self.nombre = nombre
        self.fecha = fecha
        self.bandas = []

    def inscribir_banda(self, banda):
        if any(b.nombre == banda.nombre for b in self.bandas):
            raise ValueError("Ya existe una banda con ese nombre.")
        self.bandas.append(banda)

    def registrar_evaluacion(self, nombre_banda, puntajes):
        banda = next((b for b in self.bandas if b.nombre == nombre_banda), None)
        if not banda:
            raise ValueError("Banda no encontrada.")
        banda.registrar_puntajes(puntajes)

    def listar_bandas(self):
        return [b.mostrar_info() for b in self.bandas]

    def ranking(self):
        return sorted(
            self.bandas,
            key=lambda b: b.total(),
            reverse=True
        )
class ConcursoBandasApp:
    def __init__(self):
        self.concurso = Concurso("Concurso de Bandas - 14 Septiembre", "2025-09-14")

        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Bandas - Quetzaltenango")
        self.ventana.geometry("500x400")

        self.menu()

        tk.Label(
            self.ventana,
            text="Sistema de Inscripción y Evaluación de Bandas Escolares\nConcurso 14 de Septiembre - Quetzaltenango",
            font=("Arial", 12, "bold"),
            justify="center"
        ).pack(pady=20)

        self.area_mensajes = tk.Label(self.ventana, text="", fg="blue", font=("Arial", 10))
        self.area_mensajes.pack(pady=10)

        self.ventana.mainloop()

    def mostrar_mensaje(self, texto, color="blue"):
        self.area_mensajes.config(text=texto, fg=color)

    def menu(self):
        barra = tk.Menu(self.ventana)
        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Inscribir Banda", command=self.inscribir_banda)
        opciones.add_command(label="Registrar Evaluación", command=self.registrar_evaluacion)
        opciones.add_command(label="Listar Bandas", command=self.listar_bandas)
        opciones.add_command(label="Ver Ranking", command=self.ver_ranking)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

        def inscribir_banda(self):
            ventana_inscribir = tk.Toplevel(self.ventana)
            ventana_inscribir.title("Inscribir Banda")
            ventana_inscribir.geometry("300x250")

            tk.Label(ventana_inscribir, text="Nombre de la banda:").pack()
            entry_nombre = tk.Entry(ventana_inscribir)
            entry_nombre.pack()

            tk.Label(ventana_inscribir, text="Institución:").pack()
            entry_institucion = tk.Entry(ventana_inscribir)
            entry_institucion.pack()

            tk.Label(ventana_inscribir, text="Categoría (Primaria, Básico, Diversificado):").pack()
            entry_categoria = tk.Entry(ventana_inscribir)
            entry_categoria.pack()

        def guardar():
            try:
                banda = BandaEscolar(entry_nombre.get(), entry_institucion.get(), entry_categoria.get())
                self.concurso.inscribir_banda(banda)
                self.mostrar_mensaje("Banda inscrita con éxito.", "green")
                ventana_inscribir.destroy()
            except Exception as e:
                self.mostrar_mensaje(str(e), "red")

        tk.Button(ventana_inscribir, text="Guardar", command=guardar).pack(pady=10)

        def registrar_evaluacion(self):
            ventana_eval = tk.Toplevel(self.ventana)
            ventana_eval.title("Registrar Evaluación")
            ventana_eval.geometry("350x400")

            tk.Label(ventana_eval, text="Nombre de la banda:").pack()
            entry_nombre = tk.Entry(ventana_eval)
            entry_nombre.pack()
