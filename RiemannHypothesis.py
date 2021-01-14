import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.patches import Polygon
from scipy.special import zeta
import math

'''Generate an matplotlib graph of a function with the area under the curve of the integral shaded in.
Input a function for the graph, the lower limit of the integral, the upper limit of the integral, and the optional keyword argument which will change the range of x-values on the graph.'''
def graph_integral(func, a, b, x=[-10, 10]):
	x = np.linspace(-10, 10) # x = 0 to x = 10 for the graph itself
	y = func(x)

	fig, ax = plt.subplots()
	ax.plot(x, y, 'r', linewidth=2)
	ax.set_ylim(bottom=0)

	# Illustrate area under curve
	ix = np.linspace(a, b)
	iy = func(ix)
	verts = [(a, 0), *zip(ix, iy), (b, 0)]
	poly = Polygon(verts, color = [0.72, 0, 1], edgecolor='0')
	ax.add_patch(poly)

	ax.text(0.5 * (a + b), 50, r"$f(x)=x^2$",
	        horizontalalignment='center', fontsize=20)
	ax.text(0.5 * (a + b), 30, r"$\int_0^3 f(x)\mathrm{d}x$",
	        horizontalalignment='center', fontsize=20)

	fig.text(0.9, 0.05, r'$x$')
	fig.text(0.1, 0.9, r'$y$')

	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	ax.xaxis.set_ticks_position('bottom')

	ax.set_xticks(np.arange(min(x), max(x)+1, 2.0))
	# ax.set_yticks(np.arange(min(x), max(x)+1, 2.0))

	# plt.figure(figsize=(10, 5))

	plt.show()

# graph_integral(lambda x: x**2, 0, 3)




# To do: Graph

# Zeta function:
# zeta(s) = sum(1/n^s)
# (Re(s) > 1)
def zeta_func(s, t=10000): # s is the index of the summation, t is upper limit of the summation (ideally infinity)
    equation = [1 / (n ** s) for n in range(1, t+1)] # For each term in the summation, 1/(n**s)
    return sum(equation)

# formula (20) in http://mathworld.wolfram.com/RiemannZetaFunction.html
#
# zeta(s) = 1/(1 - 2**(1-s)) * sum((-1**(n-1)) / n**s)
# Simplify
# zeta(s) = sum((-1**(n-1)) / n**s) / (1 - 2**(1-s))
def zeta_func2(s, t=10000):
    if s == 1: return float("inf") # accounting for case
    equation = [(-1)**(n-1) / (n**s) for n in range(1, t)]
    return sum(equation) / (1 - 2 ** (1-s))


# Return the binomial coefficient given an n and k
def binom(n, k):
	a = 1
	for i in range(k):
		a *= (n - i) / (i + 1) # (i + 1) to account for range starting at 0
	return a

# formula (21) in http://mathworld.wolfram.com/RiemannZetaFunction.html
# (s != 1)
# zeta(s) = (1 / (1 - 2^(1-s))) * sum(1 / 2^(n+1) * sum((-1)**k * binom(n, k) * (k+1)^-s))

# Zeta function accepts complex numbers 
def zeta_func3(s, t=100):
    if s == 1: return float("inf")
    term = [(1 / 2) ** (n + 1) * sum((-1) ** k * binom(n, k) * (k + 1) ** -s 
			for k in range(n + 1)) for n in range(t)] # Technically the value of range() should be infinite since the summation is to infinity, but it can be approximiated for the sake of runtime.
    return sum(term) / (1 - 2 ** (1 - s))

# Graph?
print(f'{abs(zeta_func3(0.5-14.134725142j)):0.10f}')

# Find the first n approximate zeroes of the Riemann Zeta function
def find_zeroes(n=10):
	zeroes = [] # Since all of the zeroes real component is 0.5, only store imaginary number
	for i in np.linspace(0, 10000, 10001):
		if len(zeroes) == 10:
			break
		val = zeta_func3(complex(0.5, i))
		if round(abs(val), 2) == 0.00:
			print('Dis one good', complex(0.5, i))

find_zeroes()