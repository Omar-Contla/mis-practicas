nombres = ["Ana", "Carlos", "Diana"]
print(nombres)

nombres.append("Elena")
print(nombres)

nombres.insert(1, "Beatriz")
print(nombres)

print("Estudiante con el indice 0 " + nombres[0])
print("Estudiante con el indice 2 " + nombres[2])

print("Diana se encuentra en el indice:", (nombres.index("Diana")))

slicing = nombres[0:3]
print("Primeros 3 estudiantes ", slicing)

slicing = nombres[1:4]
print("Subgrupo del indice 1 al 3 ", slicing)

slicing = nombres[3:4]
print("Ultimos dos estudiantes", slicing)

slicing = nombres[4::-1]
print("Lista totalmente invertida ",slicing)
