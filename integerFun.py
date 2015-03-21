######
# 
# Optional Integer Fun and Games
#
######

n = int(input('Enter a size: '))

# Print out a tree

for i in range(0, n):
	for j in range(i, n - 1):
		print(" ", end='')
	for j in range(0, i + 1):
		print (j + 1, end='')
	for j in range(i, 0, -1):
		print (j, end='')
	print ("")

# Add a trunk for fun
if n > 3:
	for i in range(0, n-1):
		print(" ", end='')
	print ("11")

# Print a checkerboard pattern
print()

for i in range(0, n):
	for j in range(0, n):
		if j%2 == i%2:
			print("X", end='')
		else:
			print("O", end='')
	print("")