import numpy as np

def matFunc(mat):
    mat = np.matrix(mat)
    mat **= 2
    return np.sum(mat)
