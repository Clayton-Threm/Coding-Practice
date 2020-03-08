#Project Euler Question 44
#Pentagon numbers

def pentagon_finder():
    pent_list = [1, 5, 12]
    x = 3
    while True:
        x += 1
        n = int(x * ((3 * x) - 1) / 2)
        pent_list.append(n)
        pent_index = -1
        while True:
            pent_index -= 1
            nb = pent_list[pent_index]
            if int(n / 2) >= nb:
                break
            nc = (n - nb)
            if nc not in pent_list:
                continue
            nd = (nb - nc)
            if nd in pent_list:
                return nd

        

print (pentagon_finder())