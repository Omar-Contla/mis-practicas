class Nodo:
    def _init_(self,dato):
        self.dato = dato
        self.siguiente = None
#CREACION DE NODO INDIVIDUAL
nodo_singular = Nodo("Primer dato")
print(nodo_singular.dato)
print(nodo_singular.siguiente)