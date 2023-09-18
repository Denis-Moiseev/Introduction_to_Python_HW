def finding_numbers(s, p):
    for x in range(1, 1001):
        y = s - x
        if x * y == p:
            return x, y
    return None, None

s = int(input("Введите сумму S: "))
p = int(input("Введите произведение P: "))

x, y = finding_numbers(s, p)

if x is not None and y is not None:
    print(f"Задуманные числа X и Y: {x}, {y}")
else:
    print("Невозможно найти подходящие числа X и Y для заданных S и P.")