class employee:
    numemps= 0
    raise_amnt= 1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@compamy.com'

        employee.numemps += 1

    def fullname(self):
        return'{} {} '.format(self.first, self.last)

    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amnt)

class developer(employee):
    raise_amnt= 1.10

    def __init__(self,first,last,pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class manager(employee):
    def __init__(self,first,last,pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        if emp in self.employees:
            print('--->', emp.fullname())


    
            
dev1= developer('Corey','Schafer',50000, 'Python')
dev2= developer('Test','User',60000, 'Java')

mng1 = manager('Sue','Smith', 90000, [dev1])

mng1.add_emp(dev2)
mng1.print_emp()

#print(dev1.email)
#print(dev1.prog_lang)


      
