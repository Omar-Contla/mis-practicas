pila = []
print("Pila inicial",pila)
for i in range(1,11):
    pila.append(i)
    print("Elemnto agregado: ",i)

print("Pila con 10 elementos: ",pila)

print("Elemento en la cima: ",pila[-1])

for i in range(4):
    elemento = pila.pop()
    print("Elemnto retirado: ",elemento)

print("Pila despues de retirar 4 elemntos: ",pila)

print("Tamaño de la pila: ",len(pila))

if len (pila) == 0:
    print("La pila esta vacia")
else:
    print("La pila no esta vacia")

while len(pila) > 0:
    elemento = pila.pop()
    print("Elemento retirado: ",elemento)

print("Pila final: ",pila)
print("La pila esta vacia: ",len(pila) == 0)