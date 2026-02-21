import sympy as sp


A = sp.Matrix([[-1, 1, -3],
               [-1, 5, 2],
               [-4, 2, 1]])

B = sp.Matrix([[-2, 2, -3],
               [-7, 4, 3],
               [4, 6, 1]])

solution_1 = A - B

solution_2 = B - A

solution_3 = 2*A + 5*B

print(solution_1)
print(solution_2)
print(solution_3)