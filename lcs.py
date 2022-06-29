def lcs(X, Y, m, n):
	if (m == 0 or n == 0):
		return 0

	if (X[m - 1] == Y[n - 1]):
		return 1 + lcs(X, Y, m - 1, n - 1)
	else:
		return max(lcs(X, Y, m, n - 1),
				lcs(X, Y, m - 1, n))

# Driver Code
if __name__ == '__main__':
	X = input("First String : ")
	Y = input("Second String : ")

	# Find the length of string
	m = len(X)
	n = len(Y)

	print("Length of LCS:",
		lcs(X, Y, m, n))
