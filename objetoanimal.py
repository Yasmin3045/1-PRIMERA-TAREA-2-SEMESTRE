class animal:
    def __init__(self, nombre, color, especie):
        self.nombre = nombre
        self.color = color
        self.especie = especie

    def hacersonido(self):
        return(f" este animal hace un sonido característico de su especie")
    def presentarse(self):
        return(f"Hola, mi nombre es {self.nombre}, soy de color {self.color} y soy un {self.especie}.")

class Perro(animal):
    def __init__(self, especie, nombre, color, raza):
        super().__init__(nombre, color, especie)
        self. raza = raza
    def hacersonido(self):
        return(f"Guau Guau")    
    def buscar (self, objeto):
        return (f"{self.nombre} está buscando la {objeto}.")

class Gato(animal):
    def __init__(self, especie, nombre, color, raza):
        super().__init__(nombre, color, especie)
        self. raza = raza
    def hacersonido(self):
        return(f"Miauuuu Miauuu")    
    def trepar_arbol(self):
        return(f"{self.nombre} está trepando un árbol.")
    def presentarse (self):
        return(f"Hola, mi nombre es {self.nombre}, soy de color {self.color} y soy un {self.especie}. Además, me gusta trepar árboles.")
    def cazar_ratones(self):
        return(f"{self.nombre} está cazando ratones.")  

class Pajaro(animal):
    def __init__(self, especie, nombre, color, tipo):
        super().__init__(nombre, color, especie)
        self.tipo = tipo
    def hacersonido(self):
        return(f"Píuuuu Píuuuuu")    
    def volar(self):
        return(f"{self.nombre} está volando en el cielo.")
    def presentarse (self):
        return(f"Hola, mi nombre es {self.nombre}, soy de color {self.color} y soy un {self.especie}. Además, me gusta volar.")
    def comer_gusanos(self):
        return(f"{self.nombre} está comiendo gusanos.")

animal1= Perro ("Perro", "Coco", "Marrón", "Labrador")
animal2=Gato("Gato", "Lulu", "Blanca ", "angora")           
animal3=Pajaro("Pájaro", "Chepe", "Azul", "Canario")
print(animal1.presentarse())
print(animal2.presentarse())
print(animal3.presentarse())
print(animal1.hacersonido())
print(animal2.hacersonido())
print(animal3.hacersonido())