from pylab import *

def g(y):
    return exp(-y)*sin(4*y)

y = np.linspace(0, 4, 501)

plt.figure()
plt.plot(y, g(y), 'r-')
plt.xlabel('y'); plt.ylabel('g(y)')
plt.title('Onde sinusoïdale atténuée')

plt.show()