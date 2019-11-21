class emp:
 
 name=[]
 def set(self):
  for i in range(0,2):
   name[i]=input("Enter name")
 def get(self):
  for i in range(0,2):
   print(name[i])

e=emp()
e.set()
e.get()
