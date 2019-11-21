try:
 a=10
 b=a/0
 print(b)

except ZeroDivisionError as y:
 print(y)
except Exception as x:
 print(x)
else:
 print("ok")  
