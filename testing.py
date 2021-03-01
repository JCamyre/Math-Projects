def convert_to_2d(arr: list):
	n = max(arr)
	nums = [[i if i <= n and arr[i] > 0 else ' ' for i in range(j, j+10)] for j in range(0, n, 10)]
	return nums 

def illustrate_nums(all_nums):
	for row in all_nums:
		print(' '.join([str(n).center(4) for n in row]))

def SieveOfEratosthenes(n: int):
    nums = [True for i in range(1, n+1)]
    p = 2 # Start with 2, as we know 1 can not be prime
    while p * p <= n: # This is how the algorithm knows when to stop testing new prime multiples
        if nums[p]: # If the current prime we are looking at doesn't have a smaller multiple
            for i in range(p*2, n, p): # All multiples of p
                nums[i] = False
        p += 1 # Checking next prime in list
    nums[0] = False # Overriding error in the code's algorithm.
    nums[1] = False
    # Returning list of all numbers. Primes have their integer value, while nonprimes are all -1.
    return [i if j else -1 for i, j in enumerate(nums)]

# Formatting lists and printing them to display them in an easy to read format. 
illustrate_nums(convert_to_2d(SieveOfEratosthenes(100)))
