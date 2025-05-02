'''
1) Código con errores para corregir

class Dog:
 def __init__(self, name):
 name = name
 def speak(self):
 return "woof"
 
dog = Dog("Bobby")
print(dog.name)

Corregir: El nombre no se guarda correctamente.

2) Ejercicio:
Define una jerarquía simple para vehículos con al menos una clase base y dos clases hijas.
Cada clase hija debe tener un método propio sobrescrito que imprima información
diferente. Crea una función que reciba un vehículo y llame a ese método.

'''

#1) Cómo guardar el nombre correctamente.

class Dog:
    def __init__(self, name):
        self.name = name
    
    def  speak(self):
        return "woof"
    
dog  = Dog("Bobby")
print(dog.name)

#2) Jerarquía de vehículos, clase base y dos hijas.
class Vehículo:
    def __init__(self, tipo_vehículo, marca, km):
        self.tipo_vehículo = tipo_vehículo
        self.marca = marca
        self.km = km
        
    def mostrar_info(self):
        print(f"{self.tipo_vehículo} de la marca {self.marca} con {self.km} Km recorridos.")
    
class Auto(Vehículo):
    def accion(self):
        print("Enciendes la radio.")
        print("Estás escuchando Bohemian Rhapsody - Queen")

class Moto(Vehículo):
    def accion(self):
        print("Giras el acelerador, la moto hace rugir su motor.")
        print("¡BRRRMMM!")
  
def realizar_accion(vehiculo):
    vehiculo.mostrar_info()
    vehiculo.accion()  
         
mi_auto = Auto("Auto", "Ford", 12000)
mi_moto = Moto("Moto", "Yamaha", 8000)

realizar_accion(mi_auto)
print("---")
realizar_accion(mi_moto)

