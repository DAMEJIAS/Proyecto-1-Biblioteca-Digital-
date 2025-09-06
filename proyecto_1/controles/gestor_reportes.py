import os

class GestorReportes:
    # Clase que genera reportes de la biblioteca y permite exportar datos en HTML

    def __init__(objeto, gestor_archivos):
        # Inicializa el gestor de reportes con el objeto que contiene préstamos, usuarios y libros
        objeto.gestor = gestor_archivos

    def historial_prestamos(objeto):
        # Muestra en consola el historial de todos los préstamos
        for a in objeto.gestor.prestamos:
            print(a)

    def usuarios_unicos(objeto):
        # Muestra en consola todos los usuarios registrados
        for b in objeto.gestor.usuarios:
            print(b)

    def libros_prestados(objeto):
        # Muestra en consola todos los libros registrados
        for c in objeto.gestor.libros:
            print(c)

    def estadisticas(objeto):
        # Calcula estadísticas de la biblioteca y las muestra en consola
        total_prestamos = len(objeto.gestor.prestamos)  # Número total de préstamos
        total_usuarios = len(objeto.gestor.usuarios)    # Número total de usuarios

        def contar_prestamos_por_libro(libro):
            # Cuenta cuántas veces se prestó un libro
            return sum(1 for p in objeto.gestor.prestamos if p.libro == libro)

        def contar_prestamos_por_usuario(usuario):
            # Cuenta cuántos préstamos realizó un usuario
            return sum(1 for p in objeto.gestor.prestamos if p.usuario == usuario)

        # Obtiene el libro más prestado y el usuario con más préstamos
        libro_mas = max(objeto.gestor.libros, key=contar_prestamos_por_libro, default=None)
        usuario_mas = max(objeto.gestor.usuarios, key=contar_prestamos_por_usuario, default=None)

        # Imprime estadísticas
        print(f"Total de préstamos: {total_prestamos}")
        print(f"Total de usuarios únicos: {total_usuarios}")
        print(f"Libro más prestado: {libro_mas}")
        print(f"Usuario más activo: {usuario_mas}")

    def prestamos_vencidos(objeto):
        # Muestra en consola los préstamos que están vencidos
        for p in objeto.gestor.prestamos:
            if p.esta_vencido():
                print(p)

    def exportar_html(objeto, carpeta="html"):

        os.makedirs(carpeta, exist_ok=True)  # Crea la carpeta si no existe

        with open(os.path.join(carpeta, "reporte.html"), "w", encoding="utf-8") as f:
            # Inicio del archivo HTML con estilos básicos
            f.write("<html><head><meta charset='UTF-8'>")
            f.write("<style>")
            f.write("table {border-collapse: collapse; width: 80%; margin: 10px 0;}")
            f.write("th, td {border: 1px solid black; padding: 8px; text-align: left;}")
            f.write("th {background-color: #f2f2f2;}")
            f.write("</style></head><body>")
            f.write("<h1>Reportes Biblioteca</h1>")

            # Historial de préstamos
            f.write("<h2>Historial de préstamos</h2>")
            f.write("<table><tr><th>Préstamo</th></tr>")
            for p in objeto.gestor.prestamos:
                f.write(f"<tr><td>{p}</td></tr>")
            f.write("</table>")

            #  Listado de usuarios únicos
            f.write("<h2>Usuarios únicos</h2>")
            f.write("<table><tr><th>Usuario</th></tr>")
            usuarios_unicos = set(p.usuario for p in objeto.gestor.prestamos)
            for u in usuarios_unicos:
                f.write(f"<tr><td>{u}</td></tr>")
            f.write("</table>")

            # Listado de libros prestados sin duplicados
            f.write("<h2>Libros prestados</h2>")
            f.write("<table><tr><th>Libro</th></tr>")
            libros_prestados = set(p.libro for p in objeto.gestor.prestamos)
            for l in libros_prestados:
                f.write(f"<tr><td>{l}</td></tr>")
            f.write("</table>")

            #Estadísticas de préstamos
            total_prestamos = len(objeto.gestor.prestamos)
            total_usuarios = len(usuarios_unicos)

            def contar_prestamos_por_libro(libro):
                return sum(1 for p in objeto.gestor.prestamos if p.libro == libro)

            def contar_prestamos_por_usuario(usuario):
                return sum(1 for p in objeto.gestor.prestamos if p.usuario == usuario)

            libro_mas = max(libros_prestados, key=contar_prestamos_por_libro, default=None)
            usuario_mas = max(usuarios_unicos, key=contar_prestamos_por_usuario, default=None)

            f.write("<h2>Estadísticas de préstamos</h2>")
            f.write("<table>")
            f.write(f"<tr><th>Total de préstamos</th><td>{total_prestamos}</td></tr>")
            f.write(f"<tr><th>Total de usuarios únicos</th><td>{total_usuarios}</td></tr>")
            f.write(f"<tr><th>Libro más prestado</th><td>{libro_mas}</td></tr>")
            f.write(f"<tr><th>Usuario más activo</th><td>{usuario_mas}</td></tr>")
            f.write("</table>")

            # Préstamos vencidos
            f.write("<h2>Préstamos vencidos</h2>")
            f.write("<table><tr><th>Préstamo</th></tr>")
            for p in objeto.gestor.prestamos:
                if p.esta_vencido():
                    f.write(f"<tr><td>{p}</td></tr>")
            f.write("</table>")

            # Cierre del HTML
            f.write("</body></html>")

        print("Reporte exportado a HTML.")
