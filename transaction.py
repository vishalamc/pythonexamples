import bal
ch=1
while ch!=4:
 print("1.Check Balance\n2.Deposit \n3.Withdrwal\n4.Exit")
 ch=int(input("Enter your choice\n"))
 if(ch==1):
  print("Balance is",bal.bal)
 if(ch==2):
  amt=int(input("Enter amount for deposit"))
  bal.bal+=amt
  print("updated balance is:",bal.bal)
 if(ch==3):
  amt=int(input("Enter amount for withdrawal"))
  if(amt<=1000):
   print("insufficient balance")
  else:
   
   bal.bal-=amt
   print("updated balance is:",bal.bal)
   
 if(ch==4):
  exit()

 ch=ch+1