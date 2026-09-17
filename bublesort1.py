lista = [60,5,18,150]
n = len (lista)
swapped = True
while swapped:
    swapped = False
for i in range(n-1):
    if lista [i]>lista [i+1]:
        lista[i], lista[i+1] = lista[i+1], lista[i]
        swapped = True
print("Lista Ordenada: ",lista)        