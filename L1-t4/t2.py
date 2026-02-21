import numpy as np

A = np.fromfunction(lambda i, j: (i + 1) - (j + 1), (3, 3), dtype=int)
print(A)