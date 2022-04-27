# -*- coding: utf-8 -*-
import random as rnd
import numpy as np
from PIL import Image
from itertools import cycle


def main():
    # Ingresar parámetros del metodo
    m = int(input("Ingresar el valor de  m: "))
    a = int(input("Ingresar el valor de  a: "))
    c = int(input("Ingresar el valor de  c: "))
    seed = rnd.randint(0, m - 1)

    # Genera y visualiza la secuencia de m-1 valores
    secuencia= genera_secuencia(m, a, c, seed, count=m, full=False, check=False)
    print("Semilla: " + str(seed))
    print(secuencia)

    # Visualización de patrones en imagen
    old_min = min(secuencia)
    old_max = max(secuencia)
    new_min = 0
    new_max = 255

    # Normalización de valores [0 - 255]
    values = [((x - old_min) * (new_max - new_min) / (old_max - old_min)) + new_min for x in secuencia]

    row = cycle(values)
    arr_img = np.array([[next(row) for i in range(0, 301)]] * 300)
    img = Image.fromarray(arr_img)
    img.show("Generador congruencial lineal")


def genera_secuencia(m, a, c, seed, count, full=True, check=True):
    seq = []
    xn = seed

    if check:
        if m < 0 or a >= m or a <= 0 or c >= m or c < 0:
            return None

    if full:
        if mcd(c, m) != 1 or not divisibile_factor_primo(a-1, m) or not ((a - 1) % 4 == 0 and m % 4 == 0):
            return None

    generador = lcg(m, a, c, seed)

    for i in range(count):
        seq.append(next(generador))

    return seq


def lcg(m, a, c, seed):
    _xn = seed

    while True:
        yield _xn
        _xn = (a * _xn + c) % m


def mcd(a, b):
    while b != 0:
        resto = a % b
        a = b
        b = resto

    return a


def factor_primo(n):
    fact = []
    d = 2

    while d*d <= n:
        while n % d == 0:
            fact.append(d)
            n /= d
        d += 1

    if n > 1:
        fact.append(n)

    return fact


def divisibile_factor_primo(a, b):
    fact_primo = factor_primo(b)

    for i in fact_primo:
        if a % i != 0:
            return False

    return True


if __name__ == "__main__":
    main()