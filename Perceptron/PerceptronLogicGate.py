import sys, os
# sys.path.append(os.pardir)
# import LogicGates
from LogicGates import BaseLogicGate
# 通过感知机实现逻辑门
class PerceptronLG(BaseLogicGate):
  def __init__(self):
    super.__init__(super())
    self.discription = "Perceptron Logic Gate"
    self.w1 = 0.5 
    self.w2 = 0.5 
    self.theta = 0.7

# AND
  def AND(self ,x ,y):
    tmp = x * self.w1 + y * self.w2
    if tmp <= self.theta:
      return 0
    elif tmp > self.theta:
      return 1
# NAND
  def NAND(self ,x ,y):
    tmp = x * (-self.w1 * x) + y * (-self.w2) + self.theta
    if tmp <= 0:
      return 0
    elif tmp > 0:
      return 1

# OR
  def OR(self ,x ,y):
    tmp = x * self.w1 + x * self.w2 - self.theta
    if tmp <= 0:
      return 0
    elif tmp > 0:
      return 1

if __name__ == "__main__" :
  perceptronLG = PerceptronLG()
  print(perceptronLG.discription)
  test_data = [[1,0],[0,1],[0,0],[1,1]]
  print("test data :",test_data)
  Gates = BaseLogicGate()
  for test in test_data:
    print("test data ", test," ",Gates.AND(test[0],test[1])," ",Gates.NAND(test[0],test[1])," ",Gates.OR(test[0],test[1]))
    # print("AND       ",(Gates.AND(test[0],test[1])))
    # print("NAND      ",(Gates.NAND(test[0],test[1])))
    # print("OR        ",(Gates.OR(test[0],test[1])))