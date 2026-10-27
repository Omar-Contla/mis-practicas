A = [[10, 15],[20, 5]]
B = [[5, 12],[15, 8]]
precio = 50

total = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
ingreso = [[total[i][j] * precio for j in range(len(total[0]))] for i in range(len(total))]

print("Total de productos vendidos (Sabado + Domingo):")
for fila in total:
    print(fila)

print("\nIngreso total en pesos (a 50 pesos por producto):")
for fila in ingreso:
    print(fila)