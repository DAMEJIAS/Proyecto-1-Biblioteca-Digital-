'''
Fabrizio bravo Morante- 1380824
Diego Alejandro Mejia Soto - 10444424
'''

from controles.gestor_archivos import GestorArchivos  # Importa el gestor de archivos
from controles.gestor_reportes import GestorReportes  # Importa el gestor de reportes

gestor = GestorArchivos()  # Crea una instancia del gestor de archivos
reportes = GestorReportes(gestor)  # Crea una instancia del gestor de reportes con el gestor

# Bucle principal del menú
while True:
        print("\n=== Menú Biblioteca Digital URL ===")
        print("1. Cargar préstamos")
        print("2. Mostrar historial de préstamos")
        print("3. Mostrar usuarios únicos")
        print("4. Mostrar libros prestados")
        print("5. Mostrar estadísticas")
        print("6. Mostrar préstamos vencidos")
        print("7. Exportar reportes a HTML")
        print("0. Salir")

        opcion = input("Seleccione una opción: ") 

        match opcion:
            case "1":
                # Cargar préstamos desde un archivo
                ruta_del_usuario = input("Ingrese la ruta del archivo: ").strip().strip('"').strip("'") 
                gestor.cargar_prestamos(ruta_del_usuario)
            case "2":
                # Mostrar historial de préstamos
                reportes.historial_prestamos()
            case "3":
                # Mostrar usuarios únicos
                reportes.usuarios_unicos()
            case "4":
                # Mostrar libros prestados
                reportes.libros_prestados()
            case "5":
                # Mostrar estadísticas
                reportes.estadisticas()
            case "6":
                # Mostrar préstamos vencidos
                reportes.prestamos_vencidos()
            case "7":
                # Exportar reportes a HTML
                reportes.exportar_html()
            case "0":
                # Salir del programa
                print("Feliz día")
                break
            case _:
                # Opción inválida
                print("Opción inválida")
