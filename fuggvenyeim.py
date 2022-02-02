import random

def szamot_beker(szoveg):
    szam = int(input(szoveg))
    return szam


def random_lista(elemszam, min, max):
    lista = []
    for n in range(elemszam):
        lista.append(random.randint(min, max))
    return lista