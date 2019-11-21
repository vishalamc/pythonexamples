pal=0
a=int(input("Enter number"))
t=a
while(t>0):
 x = t%10;
 t = t//10;
 pal = pal*10 + x;
if (pal==a):
    print("Palindrome")
else:
    print("Not a Palindrome")

