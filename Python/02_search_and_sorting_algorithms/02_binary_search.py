"""
Busqueda binaria

Algoritmo más rápido que la busqueda lineal. Este realiza una búsqueda desde el
elemento que se encuentra a la mitad de una lista ordenada. reduciendo las
opciones
"""
def binary_search(list, element):
    left, right = 0, len(list) - 1

    while left <= right:
        mid = (left + right) // 2
        if list[mid] == element:
            return mid
        elif list[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Búsqueda binaria en una lista de enteros
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_number = 7
result = binary_search(numbers_list, search_number)
print(f"1.- El elemento {search_number} se encuentra en la posición {result}")


# Búsqueda binaria en una lista de cadenas
string_list = ["banana", "manzana", "pera", "uva", "kiwi"]
element_to_search  = "pera"
result = binary_search(string_list, element_to_search)
print(f"2.- El elemento '{element_to_search}' se encuentra en la posición {result}")


# Búsqueda binaria en una lista de tuplas
tuple_list = [(1, "a"), (2, "b"), (3, "c"), (4, "d")]
element_to_search = (3, "c")
result = binary_search(tuple_list, element_to_search)
print(f"3.- El elemento {element_to_search} se encuentra en la posición {result}")


# Búsqueda binaria en una lista de números decimales
decimal_list = [1.0, 2.5, 3.7, 5.2, 6.8, 9.3]
element_to_search = 5.2
result = binary_search(decimal_list, element_to_search)
print(f"4.- The element {element_to_search} is at position {result}")


# Búsqueda binaria en una lista de booleanos
boolean_list = [False, False, True, True, True]
element_to_search = True
result = binary_search(boolean_list, element_to_search)
print(f"5.- The element {element_to_search} is at position {result}")