import matplotlib.pyplot as plt 
import numpy as np 
from scipy.integrate import quad
from matplotlib.patches import Polygon
from scipy.special import zeta
import math

def test_function(x):
	return x ** 2

ans, err = quad(test_function, 0, 1)


def graph_integral(func, a, b, x=[-10, 10]):
	a, b = 0, 3  # integral limits
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

	fig.text(0.9, 0.05, '$x$')
	fig.text(0.1, 0.9, '$y$')

	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	ax.xaxis.set_ticks_position('bottom')

	ax.set_xticks(np.arange(min(x), max(x)+1, 2.0))
	# ax.set_yticks(np.arange(min(x), max(x)+1, 2.0))

	# plt.figure(figsize=(10, 5))

	plt.show()

graph_integral(test_function, 0, 3)

# I want to program the riemann hypothesis myself so I can 

# https://gist.github.com/bellbind/529d283407e707ef3a52

# Zeta function:
# zeta(s) = sum(1/n^s)
# (Re(s) > 1)
def zeta_func(s, t=10000): # s is the index of the summation, t is upper limit of the summation (ideally infinite)
    equation = [1 / (n ** s) for n in range(1, t)] # For each term in the summation, 1/(n**s)
    return sum(equation)


print(zeta_func(2)) # => 1.6449...

# formula (20) in http://mathworld.wolfram.com/RiemannZetaFunction.html
#
# zeta(s) = 1/(1 - 2^(1-s)) * sum((-1^(n-1)) / n^s)
# Simplify
# zeta(s) = sum((-1^(n-1)) / n^s) / (1 - 2^(1-s))
def zeta2(s, t=10000):
    if s == 1: return float("inf")
    #term = ((-1)**(n - 1) / (n ** s) for n in count(1))
    #return sum(islice(term, t)) / (1 - 2**(1 - s))
    term = 
    return sum(islice(term, t)) / (2 ** (1 - s) -  1)


print(zeta2(2))
print((zeta2(2) * 6) ** 0.5)
print(abs(zeta2(0.5+14.134725142j))) # => 0
print(abs(zeta2(0.5-14.134725142j))) # => 0
#print(zeta2(0)) # invalid


# (utility) binomial coefficient
def binom(n, k):
    v = 1
    for i in range(k):
        v *= (n - i) / (i + 1)
    return v


# formula (21) in http://mathworld.wolfram.com/RiemannZetaFunction.html
# Global zeta function by Knopp and Hasse (s != 1)
def zeta3(s, t=100):
    if s == 1: return float("inf")
    term = (1 / 2 ** (n + 1) * sum((-1) ** k * binom(n, k) * (k + 1) ** -s 
                                   for k in range(n + 1)) for n in count(0))
    return sum(islice(term, t)) / (1 - 2 ** (1 - s))


print(zeta3(2))
print((zeta3(2) * 6) ** 0.5)
print(abs(zeta3(0.5+14.134725142j))) # => 0
print(abs(zeta3(0.5-14.134725142j))) # => 0
print(zeta3(1)) # => inf
print(zeta3(0)) # => -1/2
print(zeta3(-1)) # => -1/12 = 0.08333...
print(zeta3(-2)) # => 0
