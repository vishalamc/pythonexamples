def fact(n):
  if n==1:
    return n
  else:
    return n*fact(n-1)

num=int(input("Enter number"))
if num<0:
 print("not valid")
elif num==0:
 print("factorial is:",1)
else:
 print(fact(num))



