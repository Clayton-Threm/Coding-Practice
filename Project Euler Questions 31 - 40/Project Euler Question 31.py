#Project Euler Question 31
#Coin sums

def coin_comb(money):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [1] + ([0] * money)
    for coin in coins:
        for i in range(coin, (money + 1)):
            ways[i] += ways[(i - coin)]
        #print (ways)
    return ways[money]


print (coin_comb(200), "is the number of combinations")