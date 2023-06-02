class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, it's {self.name}"

class Employee(Person):
    def __init__(self, name, job_title):
        super().__init__(name)
        self.job_title = job_title
