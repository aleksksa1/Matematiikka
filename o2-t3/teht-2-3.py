import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction
pi = np.pi

x = np.linspace(-3*pi, 3*pi, 1000)

plt.figure(figsize=(12, 5))
plt.plot(x, np.sin(x), label='sin(x)', linestyle='--', color='green')
plt.plot(x, np.cos(x), label='cos(x)', linestyle=':', color='pink')

xticks = np.arange(-3*pi, 3*pi + pi/6, pi/6)
labels = []
for val in xticks:
    frac = Fraction(val / pi).limit_denominator()
    if frac.numerator == 0:
        labels.append(r"$0$")
    elif frac.denominator == 1:
        labels.append(fr"${{{frac.numerator}\pi}}$")
    else:
        labels.append(fr"$\frac{{{frac.numerator}\pi}}{{{frac.denominator}}}$")

plt.xticks(xticks, labels, rotation=45, fontsize=10)
plt.yticks([-1, 0, 1], [r"$-1$", r"$0$", r"$1$"], fontsize=10)

plt.grid(True, linestyle='--', alpha=0.3)
plt.legend()
plt.title("sin(x) ja cos(x) π/6 välein", fontsize=14)
plt.xlabel("x (radiaaneina)")
plt.ylabel("y")
plt.tight_layout()
plt.show()