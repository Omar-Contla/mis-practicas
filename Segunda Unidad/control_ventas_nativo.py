A = [[10, 15],[20, 5]]
B = [[5, 12],[15, 8]]
total_ventas = []
for i in range(2):
    fila = []
    for j in range(2):
        fila.append(A[i][j] + B[i][j])
    total_ventas.append(fila)
precio = 50
ingreso_total = []
for i in range(2):
    fila = []
    for j in range(2):
        fila.append(total_ventas[i][j] * precio)
    ingreso_total.append(fila)
print("Total de productos vendidos (Sabado + Domingo):")
for fila in total_ventas:
    print(fila)
print("\nIngreso total en pesos (a 50 pesos por producto):")
for fila in ingreso_total:
    print(fila)
