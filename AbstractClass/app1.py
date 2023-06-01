from example1 import Full_time_employee, part_time_employee, payroll

# Create a Payroll object
payroll_obj = payroll()

# Add Full_time_employee instances to the payroll
payroll_obj.add(Full_time_employee('John', 'Doe', 6000))
payroll_obj.add(Full_time_employee('Jane', 'Doe', 6500))

# Add part_time_employee instances to the payroll
payroll_obj.add(part_time_employee('Jenifer', 'Smith', 200, 50))
payroll_obj.add(part_time_employee('David', 'Wilson', 150, 100))
payroll_obj.add(part_time_employee('Kevin', 'Miller', 100, 150))

# Print the payroll information
payroll_obj.print()
