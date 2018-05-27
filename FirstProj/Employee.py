class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + "." + self.last + "@Company.com"


    def fullname(self):
        return self.first + self.last




emp1 = Employee("wajahat", "raza", 10000)
emp2 = Employee("test", "test", 12222)

print(emp1.fullname())
print(emp2.fullname())

