rev=0
n=int(input("Enter number"))
while(n!=0):
 rev=rev*10
 rev=rev+n%10
 n=n//10
print(rev)