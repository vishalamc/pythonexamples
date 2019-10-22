class faculty:
  salary=30000
  def disp1(self):
    print("Faculty avearage salary is:",self.salary)
class science(faculty):
  bonus=3000
  def disp2(self):
    self.total=self.salary+self.bonus
    print("avearage salary is :",super().salary)
    super().disp1()
    print("Science faculty :",self.total)
class computer(science):
  allowance=1000
  def disp3(self):
    self.total2=self.salary+self.bonus+self.allowance
    super().disp2()
    print("Computer faculty :",self.total2)
c=computer()
c.disp1()
c.disp2()
c.disp3()
   
