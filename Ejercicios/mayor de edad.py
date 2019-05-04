print("Digite edad: ")
edad = input()
edad = float(edad)

if edad > 17:
    print("es mayor de edad")
else:
    print("es menor de edad")

#  if de linea
print("es mayor de edad") if edad > 17 else print("es menor de edad")

# if de linea sin sino
if edad > 17: print("es mayor de edad")


#  arrays

v = ["Hola", "Mundo", 4, 3.5, True, ["Otro", "Array"]]

v2 = ["Hola", "Mundo"]

v3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

v4 = range(1, 11)

print(v2[0])  # acceder al elemento

v[1] = "yo"  # modificar elemento

v2.remove("hola")
v.pop()  # eliminar ultimo elemento
v.pop(4)  # eliminar elemento en x posicion

v.append(5)  # agregar elemento
v.append("Mundo")
v.insert(1, "yo")  # insertar en x posiv¿cion

v.index('Mundo')  # posicion de elementos
len(v)  # numero de elementos
v.count("Mundo")  # contar un elemento

a = [4, 8, 9, 7, 1]
a.sort()
res = 6 in a  # verificar elemento en un arra
print(res)

v[-1]  # ultima posicion

#  array dendro de otro array
aux = v[-2]
aux = aux[0]
print(aux)

aux = v[-2][0]

# Matriz

m = [[2, 2], [4, 1]]

# recorrer vector

v = v[2:6]  #Segementar vector
v = v[:5]  # segmentar vector

for x in v:
    print(x)

#  ciclo for

for x in v:
    print(x)

# mio
print("Digite numero final: ")
num = input()
num = int(num)
vn = range(0, num + 1)
aux = 0.0

for x in vn:
    aux = aux + x
print(aux)

print("Digite numero final: ")
num2 = int(input())
aux2 = 0
for x in range(num2+1):
    aux2 = aux2 + x
print(aux2)

#  ciclo while

i = 1
while i < 5:
    print(i)
    i = i + 1
    

