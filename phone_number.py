####
#
# Phone Number fun
#
###
import math

def sumDigits(n):
	digits = []
	sum = 0
	for i in range(0, int(math.log(n,10)) + 1):
		k = n//(10**i)
		sum += k%10

	return sum



phoneNumber = int(input ('Enter a phone number (numbers only): '))

y = phoneNumber - sumDigits(phoneNumber)

while y//10 > 0:
	y = y - sumDigits(y)

print (y)
