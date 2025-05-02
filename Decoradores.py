'''
1) Código con errores para corregir

def decorator(func):
 print("Decorating...")
 return func
 
@decorator
def greet():
 print("Hi!")
 
greet()

Corregir: Mostrar cómo se aplica realmente un decorador con un wrapper.

2) Ejercicio práctico:
Crea un decorador @authorize que solo permita ejecutar una función si un parámetro user
tiene el atributo is_admin=True. Si no, debe imprimir “Acceso denegado”. Prueba el 
decorador con una función de ejemplo.

'''

#1) Cómo se aplica realmente un decorador con un wrapper.
def decorator(function):
    def wrapper():
        print("Decorating...")
        function()
        print("Decorated!")
    return wrapper
    
@decorator
def greet():
    print("Hi!")
    
greet()

#2) Decorador @authorize
def authorize(function):
        
            def wrapper(user):
                if user.is_admin:
                    
                    print("Autorizando Acceso...")
                    function(user)
                    print("Acceso autorizado!")
                    
                else:
                    print("Acceso denegado.")
                    
            return wrapper

class User:          
    def __init__(self, name, is_admin):
        self.name = name
        self.is_admin = is_admin
    
    
@authorize
def get_data(user):
    print(f"Mostrando datos para {user.name}...")
    
    
usuario_admin = User("Oriana", True)
usuario_comun = User("Denisse", False)

get_data(usuario_admin)
print("---")
get_data(usuario_comun)



