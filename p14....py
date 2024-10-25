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

    @classmethod
    def set_raiseamnt(cls,amount):
        cls.raise_amnt = amount

    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or  day.weekday==6:
            return False
        return True
        
emp1= employee('Corey','Schafer',50000)
emp2= employee('Test','User',60000)

import datetime
mydate= datetime.date(2024, 10 ,24)
print(employee.is_workday(mydate))

      
