"""
Orden de selección (Selectión Sort)

Este algoritmo separa la lista en dos partes, ordenada y no ordenada.
Continuamente “elimina” el elemento más pequeño de la parte sin ordenar y lo
agrega a la parte ordenada.

Cuantos más elementos tengamos ordenados, menos elementos tendremos que examinar.
"""

def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]


# Orden de selección en una lista de enteros
integer_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(integer_list)
print("1.- Sorted List:", integer_list)


# Orden de selección en una lista de cadenas
string_list = ["apple", "banana", "orange", "grape", "kiwi"]
selection_sort(string_list)
print("2.- Sorted List:", string_list)


# Orden de selección en una lista de decimales
decimal_list = [3.5, 1.2, 4.8, 2.1, 0.9, 5.3]
selection_sort(decimal_list)
print("3.- Sorted List:", decimal_list)


# Orden de selección en una lista de tuplas
tuple_list = [(2, "b"), (1, "a"), (4, "d"), (3, "c")]
selection_sort(tuple_list)
print("4.- Sorted List:", tuple_list)


# Orden de selección en una lista de booleanos
boolean_list = [True, False, True, False, True]
selection_sort(boolean_list)
print("5.- Sorted List:", boolean_list)
