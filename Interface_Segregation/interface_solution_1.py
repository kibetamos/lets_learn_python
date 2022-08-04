"""The interface segregation principle advises that 
the interfaces should be small in 
terms of cohesions.

Make fine grained interfaces that are client-specific.
 Clients should 
not be forced to implement interfaces they do not use."""

from abc import ABC, abstractmethod


class Movable(ABC):
    @abstractmethod
    def go(self):
        pass

class Flyable(Movable):
    @abstractmethod
    def fly(self):
        pass
class Car(Movable):
    def go(self):
        print("Going")

class Aircraft(Flyable):
    def go(self):
        print("Taxiing")
    def fly(self):
        print("Flying")