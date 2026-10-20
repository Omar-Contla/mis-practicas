
from collections import deque
import time
cola_clientes = deque()
cola_clientes.append("Cliente 01 - CARLOS")
cola_clientes.append("Cliente 02 - MARIA")
cola_clientes.append("Cliente 03 - PEDRO")
cola_clientes.append("Cliente 04 - ANA")
print("Clientes esperando en la farmacia:")
for cliente in cola_clientes:
    print(" -", cliente)
print("\nIniciando atención en farmacia...")
while len(cola_clientes) > 0:
    cliente = cola_clientes.popleft()
    print("\nAtendiendo a:", cliente)
    time.sleep(1)
    print("Atención finalizada:", cliente)
    print("Clientes restantes:", len(cola_clientes))
print("\nTodos los clientes fueron atendidos.")
print("La fila está vacía.")