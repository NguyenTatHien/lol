class Employee:
    co_salary = 1.04
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    def Full_name(self):
        return f"{self.first_name} {self.last_name}"

    def apply_co_salary(self):
        self.pay = float(self.pay * self.co_salary)
        return self.pay

class Developer(Employee):
    co_salary = 1.5
    def __init__(self, first_name, last_name, pay, pro_lang):
        super().__init__(first_name, last_name, pay)
        self.pro_lang = pro_lang

class Secretary(Employee):
    co_salary = 1.8
    def __init__(self, first_name, last_name, pay, misson):
        super().__init__(first_name, last_name, pay)
        self.misson = misson

class Manager(Employee):
    co_salary = 2
    def __init__(self, first_name, last_name, pay, employees = None):
        super().__init__(first_name, last_name, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def Show_emp(self):
        for emp in self.employees:
            print("->>>", emp.Full_name())

    def add_employees(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        else:
            print("This emp is in list of emp")
    
    def remove_employees(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        else:
            print("This emp not in list of emp")

emp1 = Employee("Hien", "Nguyen", 1400)
emp2 = Employee("Hao", "Tran", 2000)
dev1 = Developer("Hien", "Harry", 10000, "Python")
dev2 = Developer("Han", "Kim", 4000, "C++")
dev3 = Developer("lo", "so", 3000, "Java")
dev4 = Developer("Man", "Ko", 6000, "Linux")
sec1 = Secretary("Phuong", "Nguyen", 5000, "Fuck w manager")
sec2 = Secretary("Hong", "Nguyen", 5000, "Suck a dick")
man = Manager("Logan", "Kim", 12000, [emp1, emp2, dev1, dev2, dev3, dev4, sec1])
man.add_employees(sec2)
print(dev1.Full_name)