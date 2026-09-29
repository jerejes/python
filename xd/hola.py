class persona():
    def __init__(self, nombre, edad, genero, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.ocupacion = ocupacion

    def mostrarDatos(self):        
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años, soy {self.genero} y trabajo como {self.ocupacion}.")

def llenarlista():
    nom = input("INGRESE EL NOMBRE:")
    edad = input("INGRESE LA EDAD:")
    gene = input("INGRESE EL GENERO:")
    ocp = input("INGRESE LA OCUPACION:")
    return nom,edad,gene,ocp


        


tupla = tuple()

while True:
    print("""
1:Registrar persona
2:Eliminar persona
3:Mostrar personas
4:Salir
""")
    opc = int (input("Ingrese una opción: "))
    match opc:
        case 1:
            nom,edad,gene,oco = llenarlista()
            persona = persona(nom,edad,gene,oco)
            tupla +=(persona,)
        case 2:
            for i in tupla:
                i.mostrarDatos()  
        case 3:
            print()
        case 4:
            print()
        case _:
            print()
