class emp:
  id=1234
  name="kumar"
  def __init__(self,id,name):
    self.id=id
    self.name=name
     
  def disp(self):
    return("hello")
e=emp(1,"kk")

print(e.id)
print(e.name)
print(e.disp())


