i=1
j=1
for i in range(1,5):
 for j in range(1,7):
  if(j<=2*i-1):
   print("*",end="")
  else:
   print(" ",end=" ")
 print("\r")
   