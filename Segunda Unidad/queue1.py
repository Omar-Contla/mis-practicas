from collections import deque
cola = deque()
#Agregar elementos a la cola (encolar)
cola.append("cliente 1")
cola.append("cliente 2")
cola.append("cliente 3")
#Sacar el primer elemento que llegó (desencolar)
atendido = cola.popleft()
#Mostrar resultados obtenidos
print("Atendido: ",atendido)
print("cola restante ",cola)