# 手写数字书别

import sys ,os
# sys.path.append(os.pardir)
sys.path.append(os.curdir)
from dataset.mnist import load_mnist
from PIL import Image
import numpy as np
from softmax_function import softmax
from sigmoid_function import sigmoid
import pickle

def img_show(img):
  pil_img = Image.fromarray(np.uint8(img))
  pil_img.show()

def get_data():
  (x_train,t_train), (x_test ,t_test) = load_mnist(flatten=True,normalize=False)
  return x_test, t_test

def init_network():
  with open("neural_network/sample_weight.pkl",'rb') as f:
    network = pickle.load(f)
  return network

def predict(network, x):
  w1,w2,w3 = network['W1'],network['W2'],network['W3']
  b1,b2,b3 = network['b1'],network['b2'],network['b3']

  a1 = np.dot(x,w1) + b1
  z1 = sigmoid(a1)
  a2 = np.dot(z1,w2) + b2
  z2 = sigmoid(a2)
  a3 = np.dot(z2,w3) + b3
  y  = softmax(a3)
  return y

if __name__ == "__main__":
  x, t = get_data()
  network = init_network()

  accuracy_cut = 0
  for i in range(len(x)):
    y = predict(network,x[i])
    p = np.argmax(y)
    if p == t[i]:
      accuracy_cut += 1
  print("Accuracy:"+str(float(accuracy_cut)/len(x)))