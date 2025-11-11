from datetime import date

class Pagina:
    def __init__(self, nropag, contenido):
        self.nropag = nropag
        self.contenido = contenido

    def mostrarPagina(self):
        print(f"Página {self.nropag}: {self.contenido}")

class Libro:
    def __init__(self, titulo, ISBN):
        self.titulo = titulo
        self.ISBN = ISBN
        self.paginas = [] 

    def agregarPagina(self, numero, contenido):
        pagina = Pagina(numero, contenido)
        self.paginas.append(pagina)

    def leer(self):
        for p in self.paginas:
            p.mostrarPagina()

class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrarInfo(self):
        print(f"Autor: {self.nombre} ({self.nacionalidad})")

class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def mostrarInfo(self):
        print(f"Estudiante: {self.nombre} (Código: {self.codigo})")

class Prestamo:
    def __init__(self, estudiante, libro):
        self.estudiante = estudiante
        self.libro = libro
        self.fechaprest = date.today()
        self.fechadev = None

    def mostrarInfo(self):
        print(f"Préstamo de {self.libro.titulo} a {self.estudiante.nombre} el {self.fechaprest}")

class Horario:
    def __init__(self, dias, horaApertura, horaCierre):
        self.dias = dias
        self.horaApertura = horaApertura
        self.horaCierre = horaCierre

    def mostrarHorario(self):
        print(f"Días: {self.dias}, de {self.horaApertura} a {self.horaCierre}")

class Biblioteca:
    def __init__(self, nombre, horario):
        self.nombre = nombre
        self.libros = []   
        self.autores = []    
        self.prestamos = [] 
        self.horario = horario  

    def agregarLibro(self, libro):
        self.libros.append(libro)

    def agregarAutor(self, autor):
        self.autores.append(autor)

    def prestarLibro(self, estudiante, libro):
        prestamo = Prestamo(estudiante, libro)
        self.prestamos.append(prestamo)
        print(f"Libro '{libro.titulo}' prestado a {estudiante.nombre}")

    def mostrarEstado(self):
        print(f"\nBiblioteca: {self.nombre}")
        self.horario.mostrarHorario()
        print("\nLibros disponibles:")
        for l in self.libros:
            print(f" - {l.titulo}")
        print("\nAutores registrados:")
        for a in self.autores:
            print(f" - {a.nombre}")
        print("\nPréstamos activos:")
        for p in self.prestamos:
            p.mostrarInfo()

    def cerrarBiblioteca(self):
        print(f"\n Cerrando la biblioteca {self.nombre}")
        self.prestamos.clear()
        print("todos los prestamos han sido eliminados")

horario = Horario("Lunes a Viernes", "08:00", "18:00")
biblioteca = Biblioteca("Biblioteca UMSA", horario)

libro1 = Libro("Programación en Python", "1234")
libro1.agregarPagina(1, "Introducción a Python")
libro1.agregarPagina(2, "Estructuras de Datos")

autor1 = Autor("Ana Lopez", "Boliviana")
estudiante1 = Estudiante("2025", "Manuel Limachi")

biblioteca.agregarLibro(libro1)
biblioteca.agregarAutor(autor1)
biblioteca.prestarLibro(estudiante1, libro1)
biblioteca.mostrarEstado()

biblioteca.cerrarBiblioteca()
biblioteca.mostrarEstado()
