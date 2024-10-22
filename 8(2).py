import numpy as np

N = int(input("N: "))
F = np.arange(51, 51 + N * N).reshape((N, N))
#print(F)

A = []
B = []

for i in range(N):
    for j in range(N):
        if j > i:
            A.append(F[i][j])
        elif j < i:
            B.append(F[i][j])
    
A = np.array(A)
B = np.array(B)

print(A)
print(B)