n = int(input('Введите количество кустов: '))
bushes = list()
for i in range(n):
    berries = int(input('Введите количество ягод на кусте: '))
    bushes.append(berries)

berries_per_visit = list()
for i in range(len(bushes)):
       berries_per_visit.append(bushes[i-2] + bushes[i-1] + bushes[i])
print(max(berries_per_visit))