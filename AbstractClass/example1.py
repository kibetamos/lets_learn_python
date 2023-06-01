#We need to develop a payroll program for a company.
#The company has two groups of employees: 
                                # 1.full-time employees 
                                # 2. hourly employees. 
# The full-time employees get a fixed salary while the hourly
#  employees get paid by hourly wages for their services
"""
To model the payroll program in an object-oriented way, you may come up with the following classes:
        Employee, 
        FulltimeEmployee, 
        HourlyEmployee,
         and 
        Payroll
 """
#Lets start by creating the employee class
from abc import ABC, abstractmethod
class Employee:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname 
    
    @property
    def fullname(self):
        return f"{self.firstname}{self.lastname}"
      
      
    @abstractmethod
    def get_salary(self):
        pass

    #Fulltime employee inherits from the employee

class Full_time_employee(Employee):
    def __init__(self, firstname, lastname,salary):
        super().__init__(firstname, lastname)
        self.salary = salary

    def get_salary(self):
        return self.salary

        #part time employees

        
# part_time_employee inherits from the Employee class
class part_time_employee(Employee):
    def __init__(self, firstname, lastname, worked_time, rate):
        super().__init__(firstname, lastname)
        self.worked_time = worked_time
        self.rate = rate
    
    def get_salary(self):
        return self.worked_time * self.rate
      
      
      
# payroll class manages the list of employees and their salaries
class payroll:
    def __init__(self):
        self.employee_list = []
        
    def add(self, employee):
        self.employee_list.append(employee)
    
    def print(self):
        for e in self.employee_list:
            print(f"{e.firstname} \t ${e.get_salary()}")



