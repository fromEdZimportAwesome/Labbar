import time
ordlista = open('ordlista.txt').read().split()

def linsok(lista, elem):
    return elem in lista

# while True:
#     x = input('Ditt ord: ')
#     if linsok(ordlista, x):
#         print(x, 'finns')
#     else:
#         print(x, 'finns inte')

def linsokkupp(lista):
    ordpar = []
    for ord in lista:
        if linsok(lista, ord) and linsok(lista, ord[2:5] + ord[:2]):
            ordpar.append((ord, ord[2:5] + ord[:2]))
    return ordpar
# print(linsokkupp(ordlista))

def binsok(lista, elem):
    lo = 0
    hi = len(lista) - 1
    while lo <= hi:
        mid = (lo+hi)//2
        if elem < lista[mid]:
            hi = mid - 1
        elif elem > lista[mid]:
            lo = mid + 1
        else:
            return True
    return False

def binsokkupp(lista):
    ordpar = []
    for ord in lista:
        if binsok(lista, ord) and binsok(lista, ord[2:5] + ord[:2]):
            ordpar.append((ord, ord[2:5] + ord[:2]))
    return ordpar

def sokkupp(sokfunk, lista):
    ordpar = []
    for ord in lista:
        if sokfunk(lista, ord) and sokfunk(lista, ord[2:5] + ord[:2]):
            ordpar.append((ord, ord[2:5] + ord[:2]))
    return ordpar
