# Doblar cada elemento de una lista de números.
numbers = [1,5,10,50]
result = map(lambda n1: n1 * 2, numbers)
print('1.- ', list(result))

# Convertir cada elemento de una lista de temperaturas de Celsius a Fahrenheit.
celsius_values = [15, 20, 30, 35]
result = map(lambda celsius: (celsius*9/5)+32, celsius_values)
print('2.- ', list(result))

# Calcular la longitud de cada palabra en una lista de cadenas.
words = ['Hola', 'Mundo']
result = map(lambda word:len(word), words)
print('3.- ', list(result))

# Elevar al cuadrado cada elemento de una lista de números.
result = map(lambda n1: n1 ** 2, numbers)
print('4.- ', list(result))

# Convertir a mayúsculas cada palabra en una lista de cadenas.
result = map(lambda word:word.upper(), words)
print('5.- ', list(result))
