import numpy as np
import matplotlib.pyplot as plt
# 数组运算

if __name__ == "__main__":
  one_dim_array = np.array(range(10))
  print(one_dim_array)
  print(one_dim_array * one_dim_array)
  two_dim_array = np.array([range(10),range(10)])
  two_dim_array -= 1
  print(one_dim_array * two_dim_array)
  print(two_dim_array * one_dim_array)