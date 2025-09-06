class Libro:
    # Clase que representa un libro de la biblioteca

    def __init__(mi, id_libro: str, titulo: str):
        # Inicializa un libro con su ID y título
        mi.id_libro = id_libro
        mi.titulo = titulo

    def __str__(mi):
        # Devuelve una representación en texto del libro
        return f"{mi.id_libro} - {mi.titulo}"

