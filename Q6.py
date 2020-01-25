#Q6.py
import numpy as np

def inference(param_matrix, feature_vector):
    T = param_matrix.transpose()
    X = feature_vector
    TX = t.dot(x)
    e = np.exp(TX)
    edivsume = e/np.sum(e)
    return np.log(edivsume)

t = np.arange(6).reshape(2,3)
t = t.transpose()
x = np.arange(2).reshape(2,1)
#print("tx:\n", t.dot(x))
#tx = t.dot(x)
#e = np.exp(tx)
#print("e:\n", e)
#edivsume = e/np.sum(e)
#print("e/sum(e):\n", edivsume)
#print("log(e/sum(e):\n", np.log(edivsume))

print("inference output:\n", inference(t, x))
