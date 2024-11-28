import numpy as np



k1 = 0.5
k2 = 0.3
k3 = 0.2


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
_, sigm_hat, _ = np.linalg.svd(W_hat)
val, vec = np.linalg.eig(W_hat)
W_k_norm = np.linalg.norm(W_k, 2)
W_hat_norm = np.linalg.norm(W_hat, 2)

#print(W_hat_norm/W_k_norm)
#print(1/np.sqrt(2))
print(vec[0])