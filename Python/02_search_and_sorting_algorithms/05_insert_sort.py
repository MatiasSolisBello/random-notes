"""
Tipo de inserción (Insert Sort)

Este algoritmo, al igual que la clasificación por selección, separa la lista en
dos partes, ordenadas y no ordenadas. También suponemos que el primer elemento
está ordenado, luego pasamos al siguiente elemento que lo vamos a llamar X,
comparamos X con el primero, si es mayor, se queda como está pero si es más
pequeño, copiamos el primer elemento en la segunda posición e insertamos X
como primero.
"""

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

# Orden de inserción en una lista de enteros
integer_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(integer_list)
print("1.- Sorted List:", integer_list)


# Orden de inserción en una lista de cadenas
string_list = ["apple", "banana", "orange", "grape", "kiwi"]
insertion_sort(string_list)
print("2.- Sorted List:", string_list)


#Orden de inserción en una lista de tuplas
tuple_list = [(2, "b"), (1, "a"), (4, "d"), (3, "c")]
insertion_sort(tuple_list)
print("3.- Sorted List:", tuple_list)


#Orden de inserción en una lista de booleanos
boolean_list = [True, False, True, False, True]
insertion_sort(boolean_list)
print("4.- Sorted List:", boolean_list)

# Orden de selección en una lista de decimales
decimal_list = [3.5, 1.2, 4.8, 2.1, 0.9, 5.3]
insertion_sort(decimal_list)
print("5.- Sorted List:", decimal_list)