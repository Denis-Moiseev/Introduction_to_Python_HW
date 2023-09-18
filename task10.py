string_coins = input("Введите расположение монеток через пробел (1 - решка, 2 - герб): ")

coins = string_coins.split()

sum_tails = coins.count("1")
sum_emblem = coins.count("2")

min_coin_flip = min(sum_tails, sum_emblem)
print(f"Минимальное количество переворотов: {min_coin_flip}")