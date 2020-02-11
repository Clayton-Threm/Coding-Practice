

def func_fib(x):
    n1 = 0
    n2 = 1
    n3 = 0
    list_fib = [0]
    result = 0
    for x in range(0, x):
        n3 = (n1 + n2)
        if (n3 >= 4e6):
            break
        if (n3 % 2 == 0):
            print(n1, "+", n2, "=", n3)
            list_fib.append(n3)
        n1 = n2
        n2 = n3
    print()
    print(list_fib)
    print(len(list_fib))
    print()
    for y in list_fib:
        result += y
    print(result)
        

func_fib(x = 100)