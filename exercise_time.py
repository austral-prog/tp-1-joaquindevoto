def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665

    horas=total_segundos//3600
    sobrante= total_segundos%3600
    minutos= sobrante//60
    segundos= sobrante%60

    print(horas)
    print(minutos)
    print(segundos)

