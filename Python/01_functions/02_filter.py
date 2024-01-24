# Syntex of filter: filter(function, iterable)
# The filter() function returns an iterator
# --------------------------------------------


# Filtra los números pares de una lista de enteros.
numbers = [17,24,7,39,8,51,92]
check_par = lambda n1: n1 % 2 == 0
print('1.- ', list(filter(check_par, numbers)))

# Filtra los elementos mayores que 10 de una lista de números.
check_greater_than_10 = lambda n1: n1 > 10
print('2.- ', list(filter(check_greater_than_10, numbers)))

# Filtra las palabras que empiezan con la letra 'a' en una lista de cadenas.
words = ["Alejandria", "Berlin", "Santiago", "Lima", "Tokio", "Albuquerque"]
get_started_with_a = lambda word: word[0] == 'A'
print('3.- ', list(filter(get_started_with_a, words)))

# Filtra los valores negativos de una lista de números.
new_numbers = [-1, 4, 8, 10, 30, -20, 60, -92]
get_negative_values = lambda number: number < 0
print('4.- ', list(filter(get_negative_values, new_numbers)))

# Filtra las cadenas que tienen más de 5 caracteres en una lista de palabras.
words_caracthers = lambda word: len(word) > 5
print('5.- ', list(filter(words_caracthers, words)))

# Filtra las personas mayores de 18 años en una lista de diccionarios que
# contienen información sobre ellos (nombre, edad, etc.).
people = [
    {'name': 'Juan', 'age': 25},
    {'name': 'María', 'age': 16},
    {'name': 'Carlos', 'age': 22},
    {'name': 'Ana', 'age': 28},
    {'name': 'Luis', 'age': 16}
]
get_adults = lambda person: person["age"] > 18
print('6.- ', list(filter(get_adults, people)))


# Crea una clase empleado y filtra los salarios mayores a 5000
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return "{} - ${}".format(self.name, self.salary)

listEmployee = [
    Employee("John", 35000),
    Employee("Alex", 39000),
    Employee("Matttew", 60000),
    Employee("George", 4000),
]
salary_data = filter(lambda emp:emp.salary > 5000, listEmployee)
for i in salary_data:
    print('7.- ', i)