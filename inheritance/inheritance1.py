class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, it's {self.name}"
    
    
    
class Employee(Person):
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title
        
        
        
# person = Person("Alice")
# print(person.greet())  # Output: Hi, it's Alice

# employee = Employee("Bob", "Manager")
# print(employee.greet())  # Output: Hi, it's Bob
# print(employee.job_title)  # Output: Manager


# In the example, we create an instance of Person named person with the name "Alice".
# We call the greet method on person to get a greeting message.

# Similarly, we create an instance of Employee named employee with the name "Bob" and job title "Manager". 
# We call the greet method on employee to get a greeting message and access the job_title attribute to retrieve the job title of the employee
