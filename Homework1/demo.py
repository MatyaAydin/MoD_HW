import numpy as np

W = np.arange(1, 17).reshape((4, 4))

P = np.array([
    [1, 0, 0, 0],
    [0, 0, 1, 0]
])

print(W)
print(np.dot(W, P.T))