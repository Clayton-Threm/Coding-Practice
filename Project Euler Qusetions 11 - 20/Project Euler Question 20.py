#Project Euler Question 20

#n! means n × (n − 1) × ... × 3 × 2 × 1

#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

#Find the sum of the digits in the number 100!

def factorial(x):
	if x == 1:
		return 1
	if x == 2:
		return 2
	else:
		return (x * factorial(x-1))

def digit_sum(x):
	digit_list = [int(d) for d in str(factorial(x))]
	return sum(digit_list)

print (digit_sum(100), "is the sum of the digits")