
def validar_linea(linea: str, numero_linea: int):
    # Define los caracteres permitidos
    permitidos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,- áéíóúÁÉÍÓÚñÑ"

    # Recorre cada carácter de la línea con su posición
    for i, caracter in enumerate(linea):
        # Si el carácter no está permitido y no es un salto de línea, muestra error
        if caracter not in permitidos and caracter != "\n":
            print(f"Error en línea {numero_linea}, posición {i}: carácter inválido '{caracter}'")
            return False  # Retorna falso si encuentra un carácter inválido
    
    return True  # Retorna verdadero si todos los caracteres son válidos

