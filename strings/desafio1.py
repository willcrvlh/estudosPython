import math

def delta(a, b, c):
    calculo_delta = b**2 - 4*a*c
    print (calculo_delta)

    if calculo_delta < 0:
        return print("Impossível calcular o valor de delta pois ovalor é menor que zero")
    else:
        x1 = (-b + math.sqrt(calculo_delta))/ 2*a
        x2 = (-b - math.sqrt(calculo_delta))/ 2*a
        print(x1 , x2)

delta(1, -5, 6)