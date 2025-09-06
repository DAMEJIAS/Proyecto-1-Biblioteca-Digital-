class Usuario: 
    # Clase que representa a un usuario de la biblioteca

    def __init__(mi, id_usuario: str, nombre: str):
        # Inicializa un usuario con su ID único y nombre
        mi.id_usuario = id_usuario
        mi.nombre = nombre

    def __str__(mi):
        # Devuelve una representación en texto del usuario
        return f"{mi.id_usuario} - {mi.nombre}"

