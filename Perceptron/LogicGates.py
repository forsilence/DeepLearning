# Base Logic Gatess
class BaseLogicGate:
  def __init__(self):
    self.discription = "Basic Logic Gates"
    self.bitLimit = 0b001
  
# AND gate
  def AND(self, x, y):
    x = x & self.bitLimit
    y = y & self.bitLimit
    return x & y

# NAND gate
  def NAND(self, x, y):
    x = x & self.bitLimit
    y = y & self.bitLimit
    return self.OR(~x , ~y)

  def OR(self, x, y):
    x = x & self.bitLimit
    y = y & self.bitLimit
    return x | y

if __name__ == '__main__':
  test_data = [[1,0],[0,1],[0,0],[1,1]]
  print("test data :",test_data)
  Gates = BaseLogicGate()
  for test in test_data:
    print("test data ", test)
    print("AND       ",(Gates.AND(test[0],test[1])))
    print("NAND      ",(Gates.NAND(test[0],test[1])))
    print("OR        ",(Gates.OR(test[0],test[1])))