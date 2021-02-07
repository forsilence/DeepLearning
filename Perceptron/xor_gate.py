import sys ,os
from PerceptronLogicGate import PerceptronLG
from LogicGates import BaseLogicGate

def xor(x ,y):
  # perceptron = PerceptronLG()
  # nand = perceptron.NAND(x,y)
  # or_ = perceptron.OR(x ,y)
  # res = perceptron.AND(nand ,or_)
  baselogicgates = BaseLogicGate()
  nand = baselogicgates.NAND(x ,y)
  or_ = baselogicgates.OR(x ,y)
  # print(nand ," " ,or_)
  res = baselogicgates.AND(nand,or_)
  return res

if __name__ == "__main__":
  test_data = [[1,0],[0,1],[0,0],[1,1]]
  print("test data :",test_data)
  for test in test_data:
    print(test,"->",xor(test[0],test[1]))