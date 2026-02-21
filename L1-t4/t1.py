import sympy as sp

x, y = sp.symbols('x y')

A = sp.Matrix([[x + y, 5],
               [-1, x - y]])

B = sp.Matrix([[3, 2],
               [-3, 1]])

C = sp.Matrix([[3, 5],
               [-1, 1]])

solution_AB = sp.solve(A - B, (x, y))

solution_AC = sp.solve(A - C, (x, y))

print("a)")
if not solution_AB:
    print("Ei ratkaisua")
if solution_AB:
    print(solution_AB)

print("b)")
if not solution_AC:
    print("Ei ratkaisua")
if solution_AC:
    print(solution_AC)