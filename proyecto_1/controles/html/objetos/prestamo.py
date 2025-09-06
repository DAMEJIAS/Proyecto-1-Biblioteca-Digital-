class Prestamo: 
    # Clase que representa un préstamo de un libro hecho por un usuario

    def __init__(mi, usuario, libro, fecha_prestamo: str, fecha_devolucion: str = ""):
        # Inicializa el préstamo con usuario, libro, fecha de préstamo y fecha de devolución
        mi.usuario = usuario
        mi.libro = libro
        mi.fecha_prestamo = fecha_prestamo
        mi.fecha_devolucion = fecha_devolucion

    def esta_vencido(mi):
        # Devuelve True si el préstamo ya venció, False en caso contrario
        if not mi.fecha_devolucion:
            return False  # Si no hay fecha de devolución, se considera activo
        # Fecha actual escrita manualmente (ejemplo: 2025-09-02)
        hoy = "2025-09-02"
        return mi.fecha_devolucion < hoy  # Compara la fecha de devolución con la fecha actual

    def __str__(objeto):
        # Devuelve una representación en texto del préstamo
        return f"{objeto.usuario.nombre} = {objeto.libro.titulo} ({objeto.fecha_prestamo} - {objeto.fecha_devolucion or 'NO DEVUELTO'})"
