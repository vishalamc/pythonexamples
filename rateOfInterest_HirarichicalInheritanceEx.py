class Bank:
    balance=0
    def ROI(self,amount,rate):
        self.balance=self.amount+(self.amount*self.rate)/100
        return self.balance
class SBI(Bank):
    def SBIROI(self):
        self.newbalance=super().ROI(2000,6)
        print("Rate of Interest:6%",self.newbalance)
class PNB(Bank):
    def PNBROI(self):
        self.newbalance=super().ROI(2000,7)
        print("Rate of Interest:7%",self.newbalance)

s=SBI()
p=PNB()
s.SBIROI()
p.PNBROI()
