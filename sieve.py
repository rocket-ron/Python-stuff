def primes1(n):
    """
    This method is taken from a StackOverflow question about calculation of primes performance.
    Once I saw how the sieve of Eratosthenes worked in O(n) time I was hoping to find something
    a litte more performant, so I put this method in here as a comparison. This method is from
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
    It turns out that this implementation is not Python3 compatible and runs a good 2-3 times faster
    than my sieve function
    """

    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3, int(n**0.5)+1, 2):
        if sieve[i / 2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1, n/2) if sieve[i]]


def sieve_of_eratosthenes(n):
    """
    sieve of eratosthenes

    I created this algorithm from the description in Wikipeadia http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    given a number N find all primes less than N
    We can do this by setting up a list of numbers up to N, then starting with the number 2, eliminate the multiples of
    that value. The next value to check for multiples is the next value of the list that hasn't been eliminated
    """
    import math

    np1 = n + 1
    p = [True] * np1

    # according to the Wikipeadia article on the sieve of Eratosthenes we can optimize by only going to SQRT(N)
    # we essentially truncate the floating point value then add 1
    max_value = int(math.sqrt(n)) + 1

    # using slices since I just learned how they work to mark the first two positions (0, 1) as not prime (FALSE)
    p[:2] = [False] * 2

    # this is the cool part. Starting at 2, mark all items in positions that are multiple as not prime
    # what's cool about is the combination of the optimization of starting with the square of the value (2*2, 3*3, 5*5)
    # combined with slicing using a step size - it makes for a really compact expression
    for i in range(2, max_value):
        if p[i]:
            p[i*i:np1:i] = [False] * len(range(i*i, np1, i))

    # now we can iterate the list and print the position value of those marked as prime (True)
    # for i in range(2, np1):
    #     if p[i]:
    #         print(i)

    return [i for i in range(2, np1) if p[i]]

    # So how can I build a tree in Python? I'm going to try to do this with tuples, where the items in the tuple
    # are either a factor or another tuple. That would make the leaves of the tree just the factor, but it doesn't
    # seem to be very efficient tree because we have to walk the entire tree looking for the leaves.


# This is my recursion function to walk the tuple tree and harvest the factors
def get_factors(factor_tree):
    factor_list = []
    for eachItem in factor_tree:
        if type(eachItem) is tuple:
            factor_list.extend(get_factors(eachItem))
        else:
            factor_list.extend([eachItem])
    return factor_list


def factor(n, p):
    """
    Create the tuple tree - I think there's a recursive way to do this as well
    given a number n, first check to see if it is in the list of primes
    if it is not prime, check to see if it is divisible by any of the primes using modulo operator
    if n is found to be evenly divisible, return that prime and the factor as a tuple
    if no prime is found, return n
    """
    if n not in p:
        for prime in p:
            if n % prime == 0:
                return prime, factor(int(n/prime), p)

    return n

# ---------------------------------------------------------------------------------------
#
# Prime factorization
#
# ---------------------------------------------------------------------------------------

# This is the number we want to factor
number = 1234567890

print("Calculating the sieve of Eratosthenes")
# primes = sieveOfEratosthenes(number)
primes = primes1(number)

print("factoring...")
# This is the factor tree of our number
fTree = factor(number, primes)
print (fTree)

print("Harvesting...")
# Now traverse the tree to harvest the factors
factors = get_factors(fTree)

print (factors)

uniqueFactors = set()
# Count the number of unique prime factors
for factor in factors:
    uniqueFactors.add(factor)


print ("Unique factors {}".format(len(uniqueFactors)))

