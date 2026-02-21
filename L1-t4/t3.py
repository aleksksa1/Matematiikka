import sympy as sp


A = sp.Matrix([[-1, 2],
               [3, -5]])

B = sp.Matrix([[2, 0],
               [-1, 4]])

solution_1 = 2*A + 3*B

solution_2 = A - B

print(solution_1)
print(solution_2)