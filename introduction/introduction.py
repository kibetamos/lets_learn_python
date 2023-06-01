"""
A class in python is defined by the use of a class keyword
E.g 

class Person:
    pass

person = Person()


classes are callable
we can create an object from from a class.
This is achieved by: using the class name followed by a paranthesis
e.g
    person = Person()-person is an instance of Person
Defining instance attributes
person.name = 'Jonh'
*If we create another another person object, the new object wont have a 
the name attribute.
-TO define and initialize all instances of a class we use the __init__ method
For example:
class Person:
    def __init__(self,age,name):
        self.name =name
        self.age =age
In this case, the __init__ method takes two parameters (age and name),
and it initializes the age and name attributes of the object using the values passed to the constructor.


Instance attributes are initialized by the __init__ method, the self is the
self is the instance of the person class.
**#In the __init__ method, the self is the instance of the Person class.

"""
