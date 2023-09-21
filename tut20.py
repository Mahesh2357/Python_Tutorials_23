class Organization:
    def __init__(self, name, salary):
        print('Organization : ', name)
        print('The Basic salary : ', salary)


class Benifit(Organization):
    def __init__(self,name, salary):
        super().__init__(name, salary)
        HRA = float(salary*0.10)
        print('The HRA : ', HRA)

class Benifit1(Benifit):
    def __init__(self, HRA, insentive):
        super().__init__(HRA)
        insentive = 2500
        print('The insentive : ', insentive)

class Benifit2(Benifit1):
    def __init__(self, bonus, insentive):
        super().__init__(insentive)
        bonus = 5000
        print('The Bonus : ', bonus)

class employee(Benifit2):
    def __init__(self, bonus, salary, insentive,  total_salary):
        super().__init__(bonus)
        
        self.total_salary = total_salary
        total_salary = salary + bonus + insentive
     
ow = input('Enter the Organization name : ')   
sal = input('Enter the Salary : ')   
o1 = Organization(ow, sal)

o2 = employee(100, sal, 32, 100)
# o2 = Employee()
# o1 = employee(100, 30, 1, 11)

# name = str(input("Enter name of employee : "))
# basic = float(input("Enter Basic Salary : "))
