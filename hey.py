class Employee():
    raise_amt = 1.20
    count = 0

    def __init__(self, first, last, salary):
        self.f_name = first
        self.l_name = last 
        self.salary = salary
        self.full_name = first+" "+last
        Employee.count = Employee.count+1

    def make_email(self):
        email = self.f_name+self.l_name+"@yahoo.com"
        return email

    def pay_increase(self):
        new_salary = (self.salary*self.raise_amt)
        return new_salary

class Developer(Employee):
    raise_amt = 1.24

    def __init__(self, first, last, salary, prog_language):
        Employee.__init__(self, first, last, salary)
        self.prog_language = prog_language






x = Developer("brian", "otieno", 20000, "python")
y = Developer("seth", "masibo", 30000, "java")
z = Developer("juliet", "osita", 10000, "angular")

print("new salary is;\t",x.pay_increase())
print("\nemail is;\t", x.make_email())
print(x.prog_language)      