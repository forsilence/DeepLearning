import sigmoid_function
import numpy as np
# 激活函数 ReLU Reactied Linear Unit

def ReUL(x):
  input_value = np.array(x)
  return np.maximum(0 ,x)

if __name__ == "__main__":
  test_value = np.arange(-10,10)
  print(test_value)
  output_value = ReUL(test_value)
  print("ReUL result ",output_value)
  sigmoid_function.plot_array([test_value,output_value])[0].savefig("ReLU.png")