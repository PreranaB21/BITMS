class A:
    def __init__(self,income,expend):
        self.income=income
        self.expend=expend
    def getdata(self):
        return self.income+self.expend
class B(A):
    def __init__(self,income,expend,bonus):
        super().__init__(income,expend)
        self.bonus=bonus
    def getdata(self):
        return super().getdata()+self.bonus

b=B(2000,1500,1000)
print(b.getdata())
        
        