#Project Euler Question 14

#The following iterative sequence is defined for the set of positive integers:

#n → n/2 (n is even)
#n → 3n + 1 (n is odd)

#Using the rule above and starting with 13, we generate the following sequence:

#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
#Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

#Which starting number, under one million, produces the longest chain?

#NOTE: Once the chain starts the terms are allowed to go above one million.

def collatz_sequence(num):
    collatz_list = [num]
    while num > 1:
        if num == 1:
            break
        if (num % 2 == 0):
            num = int(num / 2)
            collatz_list.append(num)
        else:
            num = ((3 * num) + 1)
            collatz_list.append(num)
    return collatz_list

def highest_collatz_length(x):
    highest_length = 0
    highest_list = []
    for x in range(1,x):
        collatz_list_check = collatz_sequence(x)
        collatz_check = len(collatz_list_check)
        if collatz_check > highest_length:
            highest_length = collatz_check
            highest_list = collatz_list_check
    #print (highest_list)
    #print (highest_length, "is the length of the list")
    #print ()
    return highest_list[0]

print (highest_collatz_length(1000000), "is the number under n that produces the longest chain")