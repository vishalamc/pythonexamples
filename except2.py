try:  
    age = int(input("Enter the age?"))  
    if age<18:  
        raise Exception;  
    else:  
        print("the age is valid")  
except Exception:  
   print("The age is not valid")  