class Counter1:
   Count = 0
  
   def count1(self):
      self.Count += 1
      print (self.Count)

class Counter2(Counter1):
   def count2(self):
     self.Count += 2
     print (self.Count)

c=Counter2()
c.count1()
c.count2()

