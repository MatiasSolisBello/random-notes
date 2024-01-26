"""
Merge Sort

Algoritmo de tipo "divide y venceras". La idea básica es dividir la lista no
ordenada en n sub-listas, cada una con un solo elemento, y luego combinar
gradualmente esas sub-listas en listas más grandes y ordenadas hasta que solo
quede una lista ordenada.
"""
def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1

# Merge Sort en una lista de enteros
integer_list = [64, 34, 25, 12, 22, 11, 90]
merge_sort(integer_list)
print("1.- Sorted List:", integer_list)

# Merge Sort en una lista de cadenas
string_list = ["apple", "banana", "orange", "grape", "kiwi"]
merge_sort(string_list)
print("2.- Sorted List:", string_list)

# Merge Sort en una lista de tuplas
tuple_list = [(2, "b"), (1, "a"), (4, "d"), (3, "c")]
merge_sort(tuple_list)
print("3.- Sorted List:", tuple_list)

#Merge Sort en una lista de booleanos
boolean_list = [True, False, True, False, True]
merge_sort(boolean_list)
print("4.- Sorted List:", boolean_list)

#Merge Sort en una lista de decimales
decimal_list = [3.2, 1.8, 4.5, 2.1, 0.9, 5.6]
merge_sort(decimal_list)
print("5.- Sorted List:", decimal_list)