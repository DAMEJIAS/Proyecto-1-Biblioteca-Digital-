from objetos.usuario import Usuario
from objetos.libro import Libro
from objetos.prestamo import Prestamo
from utils.validador import validar_linea

class GestorArchivos:
# Inicializa las listas para almacenar usuarios, libros y préstamos.
    def __init__(mi):
        mi.usuarios = []
        mi.libros = []
        mi.prestamos = []

    def cargar_prestamos(objeto, ruta: str):
        """
        Carga los préstamos desde un archivo de texto.
        Cada línea representa un préstamo con los datos separados por comas.
        """
        with open(ruta, "r", encoding="utf-8") as archivo:
            for num_linea, linea in enumerate(archivo, start=1):
                if num_linea == 1:
                    continue # Saltar encabezado

                if not validar_linea(linea, num_linea):
                    continue  # Saltar línea inválida

                partes = linea.strip().split(",")

                if len(partes) < 6:
                    print(f" Error en línea {num_linea}: formato incorrecto")
                    continue

                # Extraer los datos de la línea
                id_usuario = partes[0].strip()
                nombre = partes[1].strip()
                id_libro = partes[2].strip()
                titulo = partes[3].strip()
                fecha_prestamo = partes[4].strip()
                fecha_devolucion = partes[5].strip() if len(partes) > 5 else ""

                # Obtener o crear usuario y libro
                usuario = objeto.obtener_usuario(id_usuario, nombre)
                libro = objeto.obtener_libro(id_libro, titulo)
                # Crear el préstamo y agregarlo a la lista
                prestamo = Prestamo(usuario, libro, fecha_prestamo, fecha_devolucion)
                objeto.prestamos.append(prestamo)

                print(prestamo)

# Busca un usuario por su ID. Si no existe, lo crea y lo agrega a la lista.

    def obtener_usuario(self, id_usuario, nombre):
        for u in self.usuarios:
            if u.id_usuario == id_usuario:
                return u
        nuevo = Usuario(id_usuario, nombre)
        self.usuarios.append(nuevo)
        return nuevo
# Busca un libro por su ID. Si no existe, lo crea y lo agrega a la lista.
    def obtener_libro(self, id_libro, titulo):
        for l in self.libros:
            if l.id_libro == id_libro:
                return l
        nuevo = Libro(id_libro, titulo)
        self.libros.append(nuevo)
        return nuevo
