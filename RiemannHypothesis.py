import matplotlib.pyplot as plt 
import numpy as np 
from scipy.integrate import quad
from matplotlib.patches import Polygon


def test_function(x):
	return x ** 2

ans, err = quad(test_function, 0, 1)
print(ans)


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

	# ax.text(0.5 * (a + b), 30, r"$\int_a^b f(x)\mathrm{d}x$",
	#         horizontalalignment='center', fontsize=20)

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