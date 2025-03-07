#Operadores en Python
'''
Los operadores en python siguen el siguiente orden jerarquico:
1.     (  )
2.     **
3.     / , * , % ,
4.     + , - ,
5.     =
Nota 1:Si hay operadores con el mismo nivel de jerarquia, se resuelven de izquierda a derecha
Nota 2: Si hay parentesis dentro de parentesis se resuelve primero el parentesis interno
'''

a = 3
b = 2
c = 1
x = 5
#variables en python

y = ((2 * a + c)/ 7) * (a + (4 * a) / c)
print(y)

'''
Operadores relacionales:
Las operaciones aritmeticas resultan en un valor numerico 
Las operaciones relacionales resultan en un valor booleano:
True False (V, F SI, NO)
Operadores Relacionales:
> , < , >= , <= , == , !=
Jerarquia de operadores 
(Incluyendo los relacionales):
1.    ()
2.    **
3.    *, / , % , 
4.    + , -
5.    < , > , <= , >= , == , !=
6.    =
'''
a = 3
b = 2
c = 1
x = 5

y = c/(x+2) < c * a - c + 1 - b  * 2
print(y)
