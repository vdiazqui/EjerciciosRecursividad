def verificar_palindromo(cadena):
    # Eliminar caracteres no alfanuméricos de la cadena
    cadena_limpia = ''.join(c for c in cadena if c.isalnum())
    
    # Convertir la cadena a minúsculas para unificar el caso
    cadena_limpia = cadena_limpia.lower()
    
    # Reemplazar caracteres acentuados por sus equivalentes sin acento
    acentos = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u'}
    for original, sin_acento in acentos.items():
        cadena_limpia = cadena_limpia.replace(original, sin_acento)
    
    # Comparar la cadena con su versión invertida para determinar si es un palíndromo
    return cadena_limpia == cadena_limpia[::-1]

# Solicitar al usuario que introduzca una cadena para verificar
cadena_usuario = input("Introduce una cadena para comprobar si es un palíndromo: ")

# Realizar la verificación y mostrar el resultado
if verificar_palindromo(cadena_usuario):
    print(f'La cadena "{cadena_usuario}" es un palíndromo.')
else:
    print(f'La cadena "{cadena_usuario}" no es un palíndromo.')
