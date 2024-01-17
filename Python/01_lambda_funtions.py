# Define una función lambda que sume dos números.
exercise1 = lambda n1, n2 : n1 + n2
print('1.- ', exercise1(5,5))

# Crea una función lambda que multiplique dos números.
exercise2 = lambda n1, n2: n1*n2
print('2.- ', exercise2(5,5))

# Escribe una función lambda que calcule el cuadrado de un número
exercise3 = lambda n1: n1**2
print('3.- ', exercise3(9))

#Crea una función lambda que concatene dos cadenas de texto.
exercise4 = lambda text1, text2: f'{text1} {text2}'
print('4.- ', exercise4('Hola', 'Mundo'))

#Escribe una función lambda que verifique si un número es par.
exercise5 = lambda n1: n1 % 2 == 0
print('5.- ', exercise5(9))

#Define una función lambda que devuelva el máximo de dos números.
exercise6 = lambda n1, n2: n1 if n1 > n2 else n2
print('6.-', exercise6(10, 8))

#Crea una función lambda que calcule el área de un triángulo dado su base y altura.
exercise7 = lambda base, height: (base * height) / 2
print('7.-', exercise7(8, 5))

#Escribe una función lambda que convierta una temperatura de Celsius a Fahrenheit.
exercise8 = lambda celsius: (celsius*9/5)+32
print('8.-', exercise8(30))

#Define una función lambda que cuente la cantidad de caracteres en una cadena de texto.
exercise9 = lambda text : len(text)
print('9.- ', exercise9('Cadena'))