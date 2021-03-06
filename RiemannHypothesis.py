import matplotlib.pyplot as plt 
from matplotlib.patches import Polygon
from scipy.special import zeta
from scipy.integrate import quad
import math
import numpy as np

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

# graph_integral(lambda x: x**2, 0, 100000000)


# https://gist.github.com/bellbind/529d283407e707ef3a52

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
# Converted functions
# zeta(s) = (1 / (1 - 2^(1-s))) * sum(1 / 2^(n+1) * sum((-1)**k * binom(n, k) * (k+1)^-s))

# Zeta function accepts complex numbers 
def zeta_func3(s, t=100):
    if s == 1: return float("inf")
    term = [(1 / 2) ** (n + 1) * sum((-1) ** k * binom(n, k) * (k + 1) ** -s 
			for k in range(n + 1)) for n in range(t)] 
			# Technically the value of range() should be infinite since the summation is to infinity, but it can be approximiated for the sake of runtime.
    return sum(term) / (1 - 2 ** (1 - s)) # Equivalent to dividing the two summations and the binomial coefficient by each other
print(zeta_func3(40))

# Find the first n approximate zeroes of the Riemann Zeta function. Albeit fairly brute force. 
def find_zeroes(n=11):
	zeroes = [] # Since all of the zeroes real component is 0.5, only store imaginary number
	for i in np.linspace(0, 10000, 1000001):
		if len(zeroes) == math.ceil(n//2): # Since each zero's imaginary number can be positive or negative
			break
		val = zeta_func3(complex(0.5, i))
		if round(abs(val), 2) == 0.00:
			print(complex(0.5, i))
			zeroes.append(i)
	return zeroes

print(find_zeroes())

# Finding prime number theorem
# Returns the number of primes that are less than or equal to N
def primenum_theorem(N): # N: ℝ+
	# Multiple definitions for prime-counting function
	fig, axs = plt.subplots(2, 1, figsize=(15, 15))

	# π(N) ~ N/log(N)
	print(f'For the first {N} numbers, there are {math.floor(N/math.log10(N))} primes.')

	# Show proof for approximiation of number of primes and of nth prime number
	print(f'The nth prime number: {N * math.log10(N)}')

	# Maybe visualize Prime sieving ?
	# Graph functions?
	# x = np.linspace(1, N, 10*N)
	# y = x / np.log(x)
	# print(x, y)

	# axs[0].plot(x, y, alpha=0.4, lw=3)

	# plt.show()
	# Print all primes?

# Psuedo code for introducing how to use math in programming, then show equivalents in programming and math 

# Calculating location/number of zeros
def calculate_num_of_zeros():
	pass

# Zeros on the critical line

# Numerical calculations

# Gram points


primenum_theorem(10)


# Visualize the sieving method: "sieve of Eratosthenes"

# To find all the prime numbers less than or equal to a given integer n by Eratosthenes' method:
# 1. Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n). I created a 2d list for visualization purposes.
def create_arr(n: int):
	return [i for i in range(1, n+1)]

def convert_to_2d(arr: int):
	n = max(arr)
	nums = [[i for i in range(j, j+10) if i <= n] for j in range(2, n, 10)]
	return nums 

all_nums = generate_nums(54)
print(all_nums)

def illustrate_nums(all_nums):
	for row in all_nums:
		print(' '.join([str(n).center(4) for n in row]))
illustrate_nums(all_nums)

# Maybe too hard to do it properly, so maybe just do it the easy way
# All multiples of two
def multiples(n: int):
	# 2. Initially, let p equal 2, the smallest prime number.
	# 3. Enumerate the multiples of p by counting in increments of p from 2p to n, and mark them in the list (these will be 2p, 3p, 4p, ...; the p itself should not be marked).
	multiples_2 = [i for i in range(1, n+1) if i % 2 == 0]
	# Collapse 2d list to analyze each number. 
	print(convert_2d_list(all_nums)) # [col for row in list for col in row]. Row then col

	# 4. Find the smallest number in the list greater than p that is not marked. If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
	
	multiples_3 = [i for i in range(1, n+1) if i % 3 == 0]
	print([j for i in all_nums for j in i if j not in multiples_3])

	multiples_5 = [i for i in range(1, n+1) if i % 5 == 0]
	print([j for i in all_nums for j in i if j not in multiples_5])

	multiples_7 = [i for i in range(1, n+1) if i % 7 == 0]
	print([j for i in all_nums for j in i if j not in multiples_7])
	# 5. When the algorithm terminates, the numbers remaining not marked in the list are all the primes below n.

multiples(54)

# Visualize the multiples for each set of multiples (i.e: for the two multiples, delete all values in an array 10 x 10 from 1 to 100).


# Now all prime numbers combined (The numbers not in any of these multiples)
