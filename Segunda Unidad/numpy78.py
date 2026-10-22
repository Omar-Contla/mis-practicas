import numpy as np
#DEFINICION DE MATRICES
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
#SUMA ELEMENTO A ELEMENTO
suma = A + B
print(" ..SUMA(A + B)..")
print(suma)
#MULTIPLICACION
prod_elem = A * B
print(" ..  MULTIPLICACION(A * B)..")
print(prod_elem)
#MULTIPLICACION MATRICIAL
prod_mat = A @ B
print(" ..  PRODUCTO MATRICIAL(A @ B)..")
print(prod_mat)
#TRANSPUESTA
transpuesta = A.T
print(" ..  TRANSPUESTA(A.T)..")
print(transpuesta)
#DETERMINANTE E INVERSA
det = np.linalg.det(A)
inv = np.linalg.inv(B)
print(" ..  DETERMINANTE de A..")
print(det)
print(" ..      DETERMINANTE DE B..")
print(inv)  