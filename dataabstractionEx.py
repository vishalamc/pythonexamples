class Employee:  
    count = 0;  
    def __init__(self):  
        Employee.count = Employee.count+1  
    def display(self):  
        print("The number of employees",Employee.count)  
emp = Employee()  
emp2 = Employee()  
try:  
    print(emp.count)  
finally:  
    emp.display()  
