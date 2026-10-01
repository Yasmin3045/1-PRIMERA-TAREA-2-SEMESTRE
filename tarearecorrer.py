class ListaNumeros:
    def __init__(self):
        self.lista = []
    def agregar(self, numero):
        self.lista.append(numero)
    def mostrar(self):
        print("Mayor:", max(self.lista))
        print("Menor:", min(self.lista))
        print("Promedio:", sum(self.lista) / len(self.lista))

datos = ListaNumeros()
cantidad = int(input("¿Cuántos números va a ingresar? "))
for i in range(cantidad):
    numero = int(input("Ingrese un número: "))
    datos.agregar(numero)
datos.mostrar()
