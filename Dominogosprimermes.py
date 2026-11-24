def es_bisiesto(año: int) -> bool:
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)


def dias_en_mes(mes: int, año: int) -> int:
    if mes in (4, 6, 9, 11):
        return 30
    elif mes == 2:
        return 29 if es_bisiesto(año) else 28
    else:
        return 31


def contar_domingos_siglo_xx() -> int:
    dia_semana = 0
    domingos = 0

    for año in range(1900, 2001):
        for mes in range(1, 13):
            if año >= 1901 and dia_semana == 6:
                domingos += 1
            dias = dias_en_mes(mes, año)
            dia_semana = (dia_semana + dias) % 7

    return domingos


if __name__ == "__main__":
    resultado = contar_domingos_siglo_xx()
    print(f"Total de domingos en primer día de mes (1901-2000): {resultado}")