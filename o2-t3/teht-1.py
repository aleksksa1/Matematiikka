import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches


degrees = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])
radians = np.radians(degrees)

labels = [
    r"$\frac{\pi}{6}$", r"$\frac{\pi}{4}$", r"$\frac{\pi}{3}$", r"$\frac{\pi}{2}$",
    r"$\frac{2\pi}{3}$", r"$\frac{3\pi}{4}$", r"$\frac{5\pi}{6}$", r"$\pi$",
    r"$\frac{3\pi}{2}$", r"$2\pi$"
]

colors = plt.cm.hsv(np.linspace(0, 1, len(radians)))


fig, ax = plt.subplots()
circle = patches.Circle((0, 0), radius=1, fill=False)
ax.add_patch(circle)


ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.axis('equal')


x = np.cos(radians)
y = np.sin(radians)
ax.scatter(x, y, color=colors, marker='o')


for i in range(len(radians)):
    ax.annotate(labels[i],
                xy=(x[i], y[i]), xycoords='data',
                xytext=(20, 10), textcoords='offset points',
                fontsize=12,
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.2"))

plt.title("Yksikköympyrä radiaaneilla", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.3)
plt.show()