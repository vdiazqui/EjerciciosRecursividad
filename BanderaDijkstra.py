# Definición de constantes para los colores permitidos
ROJO, VERDE, AZUL = 'rojo', 'verde', 'azul'

def clasificar_fichas(lista_fichas):
    # Índices para las secciones de fichas rojas, verdes y la región aún no explorada
    rojo_idx = 0
    verde_idx = 0
    azul_idx = len(lista_fichas)

    # Reorganización de las fichas utilizando el enfoque de tres particiones
    while verde_idx < azul_idx:
        if lista_fichas[verde_idx] == ROJO:
            lista_fichas[rojo_idx], lista_fichas[verde_idx] = lista_fichas[verde_idx], lista_fichas[rojo_idx]
            rojo_idx += 1
            verde_idx += 1
        elif lista_fichas[verde_idx] == VERDE:
            verde_idx += 1
        else:
            azul_idx -= 1
            lista_fichas[verde_idx], lista_fichas[azul_idx] = lista_fichas[azul_idx], lista_fichas[verde_idx]
    return lista_fichas

def entrada_valida(fichas):
    # Validar que cada ficha ingresada sea de un color permitido
    colores_permitidos = {ROJO, VERDE, AZUL}
    return all(ficha in colores_permitidos for ficha in fichas)

def main():
    # Solicitar la entrada de fichas al usuario
    fichas_usuario = input(f"Ingrese las fichas separadas por espacios ({ROJO}, {VERDE}, {AZUL}): ").split()

    # Hacer una copia del orden original para mostrarlo sin alteraciones
    orden_original = list(fichas_usuario)

    if entrada_valida(fichas_usuario):
        # Clasificar las fichas y mostrar el resultado
        fichas_ordenadas = clasificar_fichas(fichas_usuario)
        print("Orden original de las fichas:", orden_original)
        print("Fichas ordenadas:", fichas_ordenadas)
    else:
        print(f"Error: Ingrese solo fichas de colores '{ROJO}', '{VERDE}' o '{AZUL}'.")

if __name__ == "__main__":
    main()
