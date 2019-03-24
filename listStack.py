stack=[1,2,3,4,5]
ch=1
while (ch!=0):
 ch=int(input("Enter your choice \n1.Push\n2.pop\n3.display"))
 if (ch==1):
   item=input("Enter Item")
   stack.append(item)
   print("item inserted")     
   
 elif (ch==2):
  stack.pop()
  print("item poped")
  
 elif (ch==3):
  print(stack)
  
 else:
  break
 ch=ch+1
	
 
	