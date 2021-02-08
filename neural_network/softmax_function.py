# softmax
import numpy as np

def softmax(x):
  c = np.max(x)
  exp_a = np.exp(x-c)
  sum_value = np.sum(exp_a)
  return exp_a/sum_value

if __name__ == "__main__":
  x = np.random.rand(5)
  print(x)
  print("softmax ",softmax(x))