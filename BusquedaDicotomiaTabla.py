# Definición de la función de búsqueda recursiva por dicotomía
def busqueda_recursiva_por_dicotomia(lista_ordenada, objetivo, inicio=0, fin=None):
    # Inicialización del final de la lista si es None
    if fin is None:
        fin = len(lista_ordenada) - 1

    # Condición de terminación: si el inicio es mayor que el fin, el objetivo no está en la lista
    if inicio > fin:
        return -1  # Objeto no encontrado

    # Cálculo del índice del medio
    medio = (inicio + fin) // 2

    # Comparación del elemento medio con el objetivo
    if lista_ordenada[medio] == objetivo:
        return medio  # Retorno del índice si se encuentra el objetivo
    elif lista_ordenada[medio] < objetivo:
        return busqueda_recursiva_por_dicotomia(lista_ordenada, objetivo, medio + 1, fin)  # Búsqueda en la sublista derecha
    else:
        return busqueda_recursiva_por_dicotomia(lista_ordenada, objetivo, inicio, medio - 1)  # Búsqueda en la sublista izquierda

# Función para manejar la entrada del usuario
def obtener_entrada_usuario():
    entrada_usuario = input("Introduce una lista ordenada de números, separados por espacios: ")
    lista_numeros = list(map(int, entrada_usuario.split()))
    elemento_a_buscar = int(input("Introduce el número a encontrar en la lista: "))
    return lista_numeros, elemento_a_buscar

# Función principal que maneja la lógica del programa
def main():
    lista_numerica, elemento_objetivo = obtener_entrada_usuario()
    # Verificación si la lista está ordenada
    if lista_numerica != sorted(lista_numerica):
        print("Error: La lista introducida no está ordenada.")
        return

    # Ejecución de la búsqueda recursiva por dicotomía
    indice_resultado = busqueda_recursiva_por_dicotomia(lista_numerica, elemento_objetivo)
    if indice_resultado != -1:
        print(f"El elemento {elemento_objetivo} se encuentra en el índice {indice_resultado}.")
    else:
        print(f"El elemento {elemento_objetivo} no se encuentra en la lista.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
