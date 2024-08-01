import timeit

def measure_time(func, data, data1):
    start_time = timeit.default_timer()
    sorted_data = func(data,data1)
    execution_time = timeit.default_timer() - start_time
    return sorted_data, execution_time


def find_coins_greedy(monet, cost):
    coins = {} 
    for i in monet:
        if cost >= i:
            count = cost // i
            cost -= count * i
            coins[i] = count
    return coins
    

def find_min_coins(monet, cost): 

    min_coins = [float('inf')] * (cost + 1)
    min_coins[0] = 0

    coin_used = [0] * (cost + 1)
    
    for coin in monet:
        for x in range(coin, cost + 1):
            if min_coins[x - coin] + 1 < min_coins[x]:
                min_coins[x] = min_coins[x - coin] + 1
                coin_used[x] = coin

    result = {}
    while cost > 0:
        coin = coin_used[cost]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        cost -= coin

    return result

monet = [50, 25, 10, 5, 2, 1]
cost = 11313

t1, t2   = measure_time(find_coins_greedy,monet,cost)
t_1, t_2 = measure_time(find_min_coins,monet,cost)

print(t1,t2)
print(t_1,t_2)


