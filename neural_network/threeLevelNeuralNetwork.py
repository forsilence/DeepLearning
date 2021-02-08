# 三层神经网络
import numpy as np
import sigmoid_function

def identity_function(x):
  return x

def init_network():
  network = {}
  network["w1"] = np.array([[0.1,0.2,0.3],[0.4,0.2,0.6]])
  network["b1"] = np.array([0.6,0.3,0.5])
  network["w2"] = np.array([[0.2,0.7],[0.5,0.3],[0.3,0.6]])
  network["b2"] = np.array([0.4,0.6])
  network["w3"] = np.array([[0.4,0.5],[0.9,0.2]])
  network["b3"] = np.array([0.3,0.8])
  return network

def forword(network,x):
  w1,w2,w3 = network["w1"],network["w2"],network["w3"]
  b1,b2,b3 = network["b1"],network["b2"],network["b3"]
  x1 = np.dot(x,w1) + b1
  x1 = sigmoid_function.sigmoid(x1)
  x2 = np.dot(x1,w2) + b2
  x2 = sigmoid_function.sigmoid(x2)
  x3 = np.dot(x2,w3) + b3
  y = identity_function(x3)
  return y

if __name__ == "__main__":
  x = np.random.randn(2)
  network = init_network()
  result = forword(network,x)
  print(result)