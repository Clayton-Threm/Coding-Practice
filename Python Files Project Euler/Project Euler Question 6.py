#The sum of the squares of the first ten natural numbers is,
#1^2+2^2+...+10^2=385
#
#The square of the sum of the first ten natural numbers is,
#(1+2+...+10)^2=55^2=3025
#
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.
#
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

high_num = 100
nums = []
sum_of_the_squares = []
for num in range(1,(high_num+1)):
    nums.append(num)
    sum_of_the_squares.append(num**2)

square_of_the_sum = (sum(nums))**2
sum_of_the_squares = sum(sum_of_the_squares)
difference = (square_of_the_sum - sum_of_the_squares)

square_of_the_sum = ("{:,}".format(square_of_the_sum))
sum_of_the_squares = ("{:,}".format(sum_of_the_squares))
difference = ("{:,}".format(difference))
high_num = ("{:,}".format(high_num))

print (difference, "is the difference between", square_of_the_sum, "and", sum_of_the_squares, "for the squares 1 -", high_num)

#the output is: 25,164,150 is the difference between 25,502,500 and 338,350 for the squares 1 - 100