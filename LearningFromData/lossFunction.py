# loss function
import numpy as np

def MeanSquaredError(x ,t):
  x = np.array(x)
  t = np.array(t)
  return 0.5 * np.sum( (x - t) ** 2 )

def CrossEntropyError(x ,t):
  delta = 1e-7
  x = np.array(x)
  t = np.array(t)
  return -np.sum(t * np.log(x + delta))

if __name__ == '__main__':
  t = [0 , 0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0]
  x = [0.1 ,0.5, 0.6 ,0.0 ,0.05 ,0.1 ,0.0 ,0.1 ,0.0 ,0.0]
  print(MeanSquaredError(x,t))
  print(CrossEntropyError(x ,t))