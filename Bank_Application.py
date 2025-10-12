class Bank:
  def __init__(self,Accounter,Amount):
    self.Accounter=Accounter
    self.Amount=Amount
  
  def __str__(self):
    return f"The Accounter Name:{self.Accounter}\n The Account Balance:{self.Amount}"
  
  def deposit(self,d_amount):
    self.Amount=self.Amount+d_amount
    print("The Amount Deposited")
    self.Balance()
  
  def withdraw(self,w_amount):
    if (self.Amount-w_amount)<0:
      print("Amount is not sufficient")
      self.Balance()
    else:
      self.Amount=self.Amount-w_amount
      print("Amount with draw successfull")
      self.Balance()
  
  def Balance(self):
    print("Balance Amount:",self.Amount)

b1=Bank("Sakthi",10000)
b1.Balance()
print(b1)
b1.deposit(5000)
b1.withdraw(2000)
b1.withdraw(20000)