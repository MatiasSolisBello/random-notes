# Detecta numeros pares
#numbers = [17,24,7,39,8,51,92]
#check_par = lambda n1: n1 % 2 == 0
#print(list(filter(check_par, numbers)))

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

# Syntex of filter: filter(function, iterable)
salary_data = filter(lambda emp:emp.salary > 5000, listEmployee)

# The filter() function returns an iterator
for i in salary_data:
    print(i)