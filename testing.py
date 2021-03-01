# 1. Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n). I created a 2d list for visualization purposes.

def convert_to_2d(arr: list):
	n = max(arr)
	nums = [[i if i <= n and arr[i] > 0 else ' ' for i in range(j, j+10)] for j in range(0, n, 10)]
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
    while p * p <= n: # This is how the algorithm knows when to stop testing new prime multiples
        if nums[p]: 
            for i in range(p*2, n, p): # All multiples of p
                nums[i] = False
        p += 1
    nums[0] = False # Overriding error in the code's algorithm.
    nums[1] = False
    # Printing numbers
    return [i if j else -1 for i, j in enumerate(nums)]

illustrate_nums(convert_to_2d(SieveOfEratosthenes(100)))
