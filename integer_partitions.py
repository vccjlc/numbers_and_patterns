# calculate the number of integer partitions. Example: p(5) = 7, because 5 = 5, 5 = 2 + 3, 5 = 4 + 1 etc.

# we use memoization and the recursive formula we found in the internet:

# p(n, k) = p(n, k-1) + p(n-k, k)

# p(n, k) is the number of ways to partition n using integers up to k

# the formula works because we add partitions excluding k and paritions with k already there 

memo = {}

def p(n, k):
	if (n < 0) or (k <= 0 and n >= 0):
		return 0
	elif n <= 1:
		return 1
	elif k == 1:
		return 1

	elif (n,k) in memo:
		return memo[(n,k)]
		
	elif k > n:
		return p(n, n)
	else:
		memo[(n,k)] = p(n, k - 1) + p(n - k, k)
		return memo[(n,k)]

def p_n(n):
	return p(n,n)

if __name__ == "__main__":
	for i in range (1, 1000):
		print(f"Number of partitions of {i} = ", p_n(i))
