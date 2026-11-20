def secuencia_collatz(n):
    pasos = 1 
    while n != 1:
        if n % 2 == 0:
            n = n // 2 
        else:
            n = 3 * n + 1
        pasos += 1
    return pasos


def buscar_maximo(limite):
    mejor_inicio = 1
    max_longitud = 1

    for inicio in range(1, limite):
        longitud = secuencia_collatz(inicio)
        if longitud > max_longitud:
            max_longitud = longitud
            mejor_inicio = inicio

    return mejor_inicio, max_longitud


if __name__ == "__main__":
    inicio_bueno, longitud_buena = buscar_maximo(1_000_000)
    print(f"Número inicial con la cadena más larga: {inicio_bueno}")
    print(f"Cantidad de términos: {longitud_buena}")

    
