"""
Busqueda lineal:

El más intuitivo de los algoritmos de busqueda, ya que compara cada uno de los
elementos de una lista(no ordenada necesariamente) hasta hallar la coincidencia.
Una de sus desventajas es que es lenta si la lista es de gran tamaño.
"""

def linear_search(numbers_list, search_number):
    for i in range(len(numbers_list)):
        if numbers_list[i] == search_number:
            return i
    return -1

# Búsqueda de un número en una lista de enteros
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_number = 7
result = linear_search(numbers_list, search_number)
print(f"1.- El elemento {search_number} se encuentra en la posición {result}")


# Búsqueda de una cadena en una lista de cadenas
word_list = ["manzana", "banana", "uva", "pera", "kiwi"]
search_word = "uva"
result = linear_search(word_list, search_word)
print(f"2.- El elemento {search_word} se encuentra en la posición {result}")


# Búsqueda de un elemento en una lista de tuplas
list_tuple = [(1, "a"), (2, "b"), (3, "c"), (4, "d")]
search_tuple = (3, "c")
result = linear_search(list_tuple, search_tuple)
print(f"3.- El elemento {search_tuple} se encuentra en la posición {result}")


# Búsqueda de un elemento en una lista de booleanos
boolean_list = [True, False, True, False, True]
search_bool = False
result = linear_search(boolean_list, search_bool)
print(f"4.- El elemento {search_bool} se encuentra en la posición {result}")