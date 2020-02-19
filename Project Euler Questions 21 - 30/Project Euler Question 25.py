#Project Euler Question 25

#The Fibonacci sequence is defined by the recurrence relation:

#Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#Hence the first 12 terms will be:

#F1 = 1
#F2 = 1
#F3 = 2
#F4 = 3
#F5 = 5
#F6 = 8
#F7 = 13
#F8 = 21
#F9 = 34
#F10 = 55
#F11 = 89
#F12 = 144
#The 12th term, F12, is the first term to contain three digits.

#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


def fib_length(length):
    fib_list = [1, 1]
    x = 2
    while x >= 0:
        fib_check = fib_list[-1] + fib_list[-2]
        fib_list.append (fib_check)
        if len(str(fib_check)) == length:
            #print (fib_list)
            #print (fib_check)
            return fib_list.index(fib_check)+1
        x += 1


print(fib_length(1000))