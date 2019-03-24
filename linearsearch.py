list1=[]
flag=0
print("Enter 5 Items in a list")
for i in range(0,5):
 item=int(input())
 list1.append(item)
print("Items in a list\n")
print(list1)
print("Enter Item to be searched")
searchitem=int(input())
for i in range(0,5):
 if(searchitem==list1[i]):
  flag=1
  break
 else:
  flag=0
if flag==1:
 print("item found in",(i+1),"position")
else:
 print("item not found")
 