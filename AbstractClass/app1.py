from example1 import Full_time_employee,part_time_employee,payroll

payroll = payroll()

payroll.add(Full_time_employee('John', 'Doe', 6000))
payroll.add(Full_time_employee('Jane', 'Doe', 6500))
payroll.add(part_time_employee('Jenifer', 'Smith', 200, 50))
payroll.add(part_time_employee('David', 'Wilson', 150, 100))
payroll.add(part_time_employee('Kevin', 'Miller', 100, 150))

payroll.print()