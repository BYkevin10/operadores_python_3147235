'''
Los operadores logicos son:
and, or, not 
obedecen las tablas de verdad:

'''
#operador and

op1 = False
op2= True
op3 = op1 and op2
print(op3)

#operador or

op4 = False
op5 = True
op6 = op4 or op5
print(op6)

#operador not

op7 = not op2
print(op7)

'''
Jerarquia definitiva de operadores 

1.    ( )
2.    **
3.    *, /, %
4.    +, -
5.    <, >, <=, >=, ==, !=
6.    NOT
7.    AND
8.    OR
9.    = 

NOTA: Si hay operaciones en el mismo nivel de jerarquia, se resuelven de izquierda a derecha
'''

op1= False
op2 = True 
op3 = False
op4 = True

resultado = not op1 and (op2 or op3 and not op1) and not op4
print(resultado)