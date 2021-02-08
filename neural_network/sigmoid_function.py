import numpy as np
import matplotlib.pyplot as plt
# 激活函数 sigmoid function
def step_function(x):
  input_value = np.array(x)
  output_value = input_value > 0.0
  return output_value.astype(np.int)

def sigmoid(x):
  output_value = np.zeros(len(x))
  for it in range(len(x)):
    if x[it] >= 0:
      output_value[it] = 1/(1 + np.exp(-x[it]))
    else:
      output_value[it] = np.exp(x[it])/(1+np.exp(x[it]))
  return output_value

def plot_array(x,fig_axis=None):
  if fig_axis is None:
    fig_axis = plt.subplots()
  fig_axis[1].plot(x[0],x[1])
  return fig_axis

if __name__ == '__main__':
  test_value = np.arange(-10,10)
  print(test_value)
  result_value = step_function(test_value)
  print("step function ",result_value)
  sigmoid_result = sigmoid(test_value)
  print("sigmoid       ",sigmoid_result)
  plot_a = plot_array([test_value,result_value])
  plot_array([test_value,sigmoid_result],plot_a)
  plot_a[0].savefig("fig.png")
