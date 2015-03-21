def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]

def sieveOfEratosthenes(n):
# sieve of eratosthenes
#
# given a number N find all primes less than N
# We can do this by setting up a list of numbers up to N, then starting with the number 2, eliminate the multiples of that value.
# The next value to check for multiples is the next value of the list that hasn't been elimuinated
    import math

    np1 = n + 1
    p = [True] * np1

    # according to the Wikipeadia article on the sieve of Eratosthenes we can optimize by only going to SQRT(N)
    # we essentially truncate the floating point value then add 1
    maxValue = int(math.sqrt(n)) + 1

    # using slices since I just learned how they work to mark the first two positions (0, 1) as not prime (FALSE)
    p[:2] = [False] * 2

    # this is the cool part. Starting at 2, mark all items in positions that are multiple as not prime
    # what's cool about is the combination of the optimization of starting with the square of the value (2*2, 3*3, 5*5)
    # combined with slicing using a step size - it makes for a really compact expression than if I had used Java, C# or C++
    for i in range(2, maxValue):
	    if p[i]:
		    p[i*i:np1:i] = [False] * len(range(i*i, np1, i))

    # now we can iterate the list and print the position value of those marked as prime (True)
 #   for i in range(2, np1):
 #       if p[i]:
 #           print(i)

    return [i for i in range(2, np1) if p[i]]

# So how can I build a tree in Python? I'm going to try to do this with tuples, where the items in the tuple are either a factor or another tuple.
# That would make the leaves of the tree just the factor, but it doesn't seem to be very efficient tree because we have to walk the entire tree 
# looking for the leaves. But it's a place to start

# This is my recusion function to walk the tuple tree and harvest the factors
def getFactors(factorTree):
	factorList = []
	for eachItem in factorTree:
		if type(eachItem) is tuple:
			factorList.extend(getFactors(eachItem))
		else:
			factorList.extend([eachItem])
	return factorList


# Create the tuple tree - I think there's a recursive way to do this as well 
# given a number n, first check to see if it is in the list of primes
# if it is not prime, check to see if it is divisible by any of the primes using modulo operator
# if n is found to be evenly divisible, return that prime and the factor as a tuple
# if no prime is found, return n
def factor(n, primes):
	if n not in primes:
		for prime in primes:
			if n % prime == 0:
				return (prime, factor(int(n/prime), primes))

	return n

#---------------------------------------------------------------------------------------
#
# Prime factorization
#
#---------------------------------------------------------------------------------------

# This is the number we want to factor
number = 1234567890

print("Calculating the sieve of Eratosthenes")
primes = sieveOfEratosthenes(number)
#primes = primes(number)

print("factoring...")
# This is the factor tree of our number
fTree = factor(number, primes)

print("Harvesting...")
# Now traverse the tree to harvest the factors
factors = getFactors(fTree)

print (fTree)
print (factors)
