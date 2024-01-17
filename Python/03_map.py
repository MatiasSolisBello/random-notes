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

def calculate_new_salary(emp):
    emp.salary=emp.salary*1.03
    return emp

list_new_salarys=map(calculate_new_salary, listEmployee)
for i in list_new_salarys:
    print(i)