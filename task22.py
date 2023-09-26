n = int(input("Введите количество элементов первого набора цифр: "))
m = int(input("Введите количество элементов второго набора цифр: "))

set1 = set()
set2 = set()

print("Введите поочередно элементы первого набора цифр:")
for i in range(n):
    element = int(input())
    set1.add(element)

print("Введите поочередно элементы второго набора цифр:")
for i in range(m):
    element = int(input())
    set2.add(element)

common_elements = sorted(set1.intersection(set2))

print("Общие элементы без повторений в порядке возрастания:")
for element in common_elements:
    print(element)