class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, it's {self.name}"

class Employee(Person):
    def __init__(self, name, job_title):
        # Call the __init__ method of the Person class to initialize the name attribute
        super().__init__(name)
        self.job_title = job_title

# Create an instance of the Employee class
employee = Employee("John Doe", "Software Engineer")
print(employee.name)  # Output: John Doe
print(employee.job_title)  # Output: Software Engineer
print(employee.greet())  # Output: Hi, it's John Doe
