row=5
star=1
space=8
for i in range(1,row+1):
 print("\r")
 for k in range(1,space+1):
  print(" ",end="")
 for j in range(1,star+1):
  print("*",end="")
 space=space-1
 star=star+2
 
 
 
