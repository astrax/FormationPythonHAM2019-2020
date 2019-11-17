from pylab import *
from racines import EqSecondDegree
def f(x):
    return 0.83 * x**2 + 3.8 * x + 2.48
x = linspace(-6, 1, 200)
y = f(x)
x1, x2 = EqSecondDegree(0.83, 3.8, 2.48)

figure(figsize=(7, 5), dpi=80)
plot(x, y, color="blue", linewidth=3, linestyle="-", alpha=.8) 
scatter([x1,x2], [f(x1), f(x2)], 80, color='red')
annotate('x1= {:.2f}'.format(x1),
             xy=(x1, f(x1)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
annotate('x2= {:.2f}'.format(x2),
             xy=(x2, f(x2)), xycoords='data',
             xytext=(+40, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
suptitle("Racines d’une équation du second degré", fontweight= 'bold')
title(r"$f(x) = 0.83 * x^2 + 3.8 * x + 2.48$",fontsize=14, color = 'r')
plt.grid()

plt.savefig("equation2deg.png"); plt.savefig("equation2deg.pdf")
plt.show()