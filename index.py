import math

# 1 Comentarios

# 1.2 cometario de linea
"""
1.3 comentario de parrafo
"""

# 2 hola mundo

print('Hello world')

# 3 variables

x = 4   # int
y = "texto"  # string
z = 4.5  # float
a = True  # boolean
b = False  # boolean
c = 4 + 5j   # complejo

print(x, y, z, a, b, c)

# 3.1 conocer tipo de dato
print(type(b))

# 4 conversiones de tipos de datos

# 4.1 enteros

x = int(2)
print(x)
x = int(2.8)
print(x)
x = int("2")
print(x)

# 4.2 Flotantes

x = float(2)
print(x)
x = float(2.8)
print(x)
x = float("2")
print(x)
x = float("2.5")
print(x)

# 4.3 Cadenas

x = str(2)
print(x)
x = str(2.8)
print(x)
x = str("2")
print(x)
x = str("2.5")
print(x)

# 5 manejo de cadenas de texto y algunos datos

cad = "Hello World"
print(cad[3])
print(cad[0:5])

cad = "       Hello World      "
cad = cad.strip()
print(cad)
print(cad[0])

cad = "Hello World"
print(len(cad))
print(cad.lower())
print(cad.upper())

print(cad.replace('l', 'y'))
print(cad.split(" "))
print(cad.split("l"))

# 6 Operaciones

# 6.1 Operaciones Aritmeticas

a = 2
b = 3
c = a + b
c = a - b
c = a * b
c = a / b  # cociente
c = a // b  # parte entera
c = a % b  # reciduo
c = a ** b  # Exponente
c = math.sqrt(a)  # raiz

# 7 capturar datos

print("Digite el nombre: ")
nombre = input()
print("Hola "+nombre+"!")

print("Digite numero uno: ")
n1 = input()
n1 = float(n1)
print("Digite numero dos: ")
n2 = input()
n2 = float(n2)
print(n1 + n2)

# 8 Condiciones

a = 2
b = 4

if a > b:
    print(a, "es mayor que", b)
else:
    print(b, "es mayor que", a)

if b > a:
    if b > 1:
        print(b, "es mayor que 1 y mayor que", a)

if a == b:
    print("Son iguales")
elif a > b:
    print(a, "es mayor que", b)
else:
    print(b, "es mayor que", a)

if a == b and a >2:
    print(a, "es mayor que 2 e igual a", b)
