"""
Quicksort

Algoritmo de ordenamiento eficiente basado en la estrategia de
"dividir y venceras". El algoritmo selecciona un elemento de la lista como
pivote y reorganiza los demás elementos en torno a él, de manera que los
elementos más pequeños quedan a su izquierda y los elementos más grandes a su
derecha. Luego, el pivote se coloca en su posición final. Este proceso se repite
recursivamente para las sublistas izquierda y derecha hasta que toda la lista
esté ordenada.
"""

def quicksort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        less = [x for x in lst[1:] if x <= pivot]
        greater = [x for x in lst[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# Quicksort en una lista de enteros
integer_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = quicksort(integer_list)
print("1.- Sorted List:", sorted_list)


#Quicksort en una lista de cadenas
string_list = ["apple", "banana", "orange", "grape", "kiwi"]
sorted_list = quicksort(string_list)
print("2.- Sorted List:", sorted_list)


#Quicksort en una lista de tuplas
tuple_list = [(2, "b"), (1, "a"), (4, "d"), (3, "c")]
sorted_list = quicksort(tuple_list)
print("3.- Sorted List:", sorted_list)


#Quicksort en una lista de decimales
decimal_list = [3.2, 1.8, 4.5, 2.1, 0.9, 5.6]
sorted_list = quicksort(decimal_list)
print("4.- Sorted List:", sorted_list)


#Quicksort en una lista de booleanos
boolean_list = [True, False, True, False, True]
sorted_list = quicksort(boolean_list)
print("5.- Sorted List:", sorted_list)