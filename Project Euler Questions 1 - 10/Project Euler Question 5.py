#Project Euler Queestion 5

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

highest_factor = 20
factor = highest_factor
x = highest_factor
while x >= 0:
    if (x % factor == 0):
        if (factor == 2):
            smallest_multiple = x
            factor = highest_factor
            break
        else:
            factor -= 1
    else:
        x += highest_factor
        factor = highest_factor
#for factor in range(highest_factor,0,-1):
	#print(smallest_multiple, "/", factor, "=", (int(smallest_multiple/factor)))
#print()

print (smallest_multiple, "is the smallest number that is evenly divisible by every number from 1 to", highest_factor)