'''
Condicional:
Es una expresion que al ser evaluada da como resultado un valor verdadero o falso.
Por lo tanto, en una condicional debe haber operadores relacionales o logicos 
'''
#Ejemplo de Condicional

a = 3
b = 2
c = 1
d = 4

resultado = not (a ** 2 - b > c ** 2) and ((a * 3 + c)/ 2 < d) or True
print(resultado)

x = 5
y = 10
z = 5

resultado =(x == z + (8 + z)) and not ((y + 3) * (4 / (z + 1))) == z
print(resultado)