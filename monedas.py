lista = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05]
vuelto = float(input("INGRESE EL VUELTO"))
lista2 = []
total = vuelto
for iter, i in enumerate(lista):
    while total > i:
        if (total > i):
            lista2.insert(iter, i)
            total -= i
num = 0
for i in lista:
    if total < i and total > 0:
        num = i
if num > 0:
    lista2.insert(len(lista)-1, num)
print(lista2)

for i in lista:
    cantidad = lista2.count(i)

    if cantidad > 0:
        print(f"{cantidad} de S/{i}")
