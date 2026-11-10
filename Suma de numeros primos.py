def suma_primos_hasta(limite):
    es_primo = [True] * limite
    es_primo[0] = es_primo[1] = False  
    
    for p in range(2, int(limite**0.5) + 1):
        if es_primo[p]:
            for i in range(p * p, limite, p):
                es_primo[i] = False
    return sum(i for i, primo in enumerate(es_primo) if primo)


limite = 2_000_000
resultado = suma_primos_hasta(limite)

print(f"La suma de los números primos menores a {limite} es: {resultado}")