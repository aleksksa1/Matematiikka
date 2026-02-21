import sympy as sp


A = sp.Matrix([[4, 9, 0],
               [-3, 7, -11]])

B = sp.Matrix([[8, 9],
               [-3, 12],
               [0, -1],
               [7, 1]])

Atranspoosi = sp.transpose(A)
Btrasnpoosi = sp.transpose(B)

print(Atranspoosi)
print(Btrasnpoosi)