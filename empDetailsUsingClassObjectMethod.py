class emp:
    name=[]
    dict={}
    id=[]
    def setDetails(self):
        
        for i in range(0,3):
            print("Enter name")
            self.item=input()
            self.key=self.item
            self.name.append(self.item)
            print("Enter id")
            self.item2=input()
            self.value=self.item2
            self.id.append(self.item2)
            self.dict[self.key]=self.value

    def getDetails(self):
        
        print("Name","\t","Id")
        for i in range(0,3):
            
            print(self.name[i],"\t",self.id[i])
        print(self.dict)
                    

e=emp()
e.setDetails()
e.getDetails()
