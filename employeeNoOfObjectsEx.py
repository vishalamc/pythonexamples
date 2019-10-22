class employee:
 count=0
 def __init__(self):
   employee.count=employee.count+1
   
     
emp1=employee()
emp2=employee()
emp3=employee()
print("The number of objects:",employee.count)  
print(getattr(emp1,'count'))  
