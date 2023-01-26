class calculator():
  
  def __init__( self, x, y ):
    self.x = x
    self.y = y

  def add(self):
      return  self.x + self.y 

  def subtraction(self):
      return self.x - self.y

  def multiplication(self):
    return self.x * self.y

  # def division(self):

  #   try:
  #     return self.x / self.y  
    
  #   except:
  #     raise err