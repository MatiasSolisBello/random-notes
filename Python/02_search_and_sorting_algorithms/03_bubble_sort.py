"""
Ordenamiento de burbuja (Bubble Sort)

Algoritmo mas sencillo de implementar, funciona intercambiando repetidamente los
elementos de una lista si se encuentra en un orden incorrecto
"""
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if isinstance(lst[j], (int, float)) and isinstance(lst[j + 1], (int, float)):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]

#Ordenamiento de burbuja en una lista de enteros
integer_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(integer_list)
print("1.- Sorted List:", integer_list)


# Ordenamiento de burbuja en una lista de cadenas
string_list = ["apple", "banana", "orange", "grape", "kiwi"]
bubble_sort(string_list)
print("2.- Sorted List:", string_list)


#Ordenamiento de burbuja en una lista de tuplas
tuple_list = [(2, "b"), (1, "a"), (4, "d"), (3, "c")]
bubble_sort(tuple_list)
print("3.- Sorted List:", tuple_list)


# Ordenamiento de burbuja en una lista mixta
mixed_list = [3, "apple", 1.5, (4, "kiwi"), 2.0]
bubble_sort(mixed_list)
print("4.- Sorted List:", mixed_list)

# Ordenamiento de burbuja en una lista de booleanos
boolean_list = [True, False, True, False, True]
bubble_sort(boolean_list)
print("5.- Sorted List:", boolean_list)