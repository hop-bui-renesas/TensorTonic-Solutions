import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    res = 1/(1+np.exp(-np.array(x)))
    return res