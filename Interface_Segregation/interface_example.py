from abc import ABC, abstractmethod

class Vehicle:
    @abstractmethod
    def go(self):
        pass
    @abstractmethod

    def fly(self):
        pass
class Aircraft(Vehicle):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")

class Car(Vehicle):
    def go(self):
        print("Going")

    def fly(self):
        raise Exception('The car cannot fly')
"""
this design violates the interface segregation principle.
"""
# In this design the Car class must implement the fly() method from 
# the Vehicle class that the Car class doesn’t use. 
# Therefore, 
# this design violates the interface segregation principle.
#SOLUTION#
#check solution from interface_solution_1.py"

