def fab(n):
  if n<=1:
    return n
  else:
    return fab(n-1)+fab(n-2)
num=int(input("Enter limit"))
for i in range(0,num+1):
  print(fab(i))
sum=0
for j in range(1,num+1):
  sum=sum+fab(j)
print(sum)
  
  