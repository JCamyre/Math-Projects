# 1. Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n). I created a 2d list for visualization purposes.

def convert_to_2d(arr: int):
	n = max(arr)
	nums = [[i for i in range(j, j+10) if i <= n] for j in range(2, n, 10)]
	return nums 

def illustrate_nums(all_nums):
	for row in all_nums:
		print(' '.join([str(n).center(4) for n in row]))
# illustrate_nums(all_nums)

# Maybe too hard to do it properly, so maybe just do it the easy way
# All multiples of two
def SieveOfEratosthenes(n: int):
    nums = [True for i in range(1, n+1)]
    p = 2
    while p * p <= n: # Illustrate this part
        if nums[p]: 
            for i in range(p*2, n, p): # All multiples of p
                nums[i] = False
        p += 1
    nums[0] = False
    nums[1] = False
    # Printing numbers
    print([i if j else ' ' for i, j in enumerate(nums)])


SieveOfEratosthenes(100)

