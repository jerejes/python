class usuario ():
    nombre = None
    apellido = None
    edad = None
    sueldo = None

    def __init__(self, nom, ape, eda, sueld):
        self.nombre = nom
        self.apellido = ape
        self.edad = eda
        self.sueldo = sueld

    def mostrar(self):
        print(f"""\nNOMBRE:{self.nombre}
              \nAPELLIDO:{self.apellido}
              \nEDAD:{self.edad} 
              \nSUELDO:{self.sueldo}""")

    def aumento(self, porcen):
        porcen /= 100
        self.sueldo += self.sueldo*porcen
        return self.sueldo


areglo = tuple()
while True:
    print("""========== SISTEMA DE USUARIOS ==========
                        1. Registrar usuario
                        2. Mostrar usuarios
                        3. Mostrar un usuario
                        4. Aumentar sueldo
                        5. Salir
                        Seleccione una opción:""")
    opc = int(input("ELIJA UNA OPCION:"))
    match opc:
        case 1:
            nom = input("Ingrese su nombre:")
            apellido = input("Ingrese su apellido:")
            edad = int(input("Ingrese su edad:"))
            sueldo = float(input("Ingrese su sueldo:"))
            usua = usuario(nom, apellido, edad, sueldo)
            areglo += (usua,)

        case 2:
            print("----MOSTRANDO DATOS----")
            for indice, i in enumerate(areglo):
                print(f"\nUSUARIO {indice+1}")
                i.mostrar()
                print("--------------------")
            print("----------FINAL----------")
        case 3:
            elecusu = int(input("INGRESE LA POSICION DEL USUARIO:"))-1
            for indice, i in enumerate(areglo):
                if elecusu == indice:
                    i.mostrar()
        case 4:
            elecusu = int(input("INGRESE LA POSICION DEL USUARIO:"))-1
            aumento = float(input("INGRESE EL PORCENTAJE DE AUMENTO:"))
            for indice, i in enumerate(areglo):
                if elecusu == indice:
                    i.aumento(aumento)
        case 5:
            print("ADIOS")
            break
        case _:
            print("INGRESE UNA OPCION VALIDA")
