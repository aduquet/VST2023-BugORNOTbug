class calculator():
  def __init__(self,x,y):
    self.x=x
    self.y=y

  def add(self):
    print("Sum :",self.x+self.y)

  def subtraction(self):
    print("Subtraction :",self.x-self.y)  

  def multiplication(self):
    print("Multiplication :",self.x*self.y)

  def division(self):
    print("Division :",self.x/self.y)  

# n = calculator(10, 4)
# n.subtraction()