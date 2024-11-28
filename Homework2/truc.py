import numpy as np



k1 = 8
k2 = 4
k3 = 5


W_k = np.array([
    [k2, k3, 0, k1],
    [k1, k2, k3, 0],
    [0, k1, k2, k3],
    [k3, 0, k1, k2]
])

W_hat = np.array([
    [k2, k3, 0, k1],
    [0, k1, k2, k3]
])


_, sigm_k, _ = np.linalg.svd(W_k)
#lambd_k , _ = np.linalg.eig(W_k)
_, sigm_hat, _ = np.linalg.svd(W_hat)

print(sigm_k) #sqrt(36), sqrt(8), sqrt(8), sqrt(4) si k1 = 1, k2 = 2, k3 = 3
print(sigm_hat) #sqrt(20), sqrt(8)
#print(lambd_k)

#print(sigm_hat[0]/sigm_k[0])