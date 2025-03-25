'''Задача 1. Фильтр конвейера с батончиками'''

result_good = []

while True:
    mass = int(input())
    if mass == 0:
        break
    if 40 <= mass <= 50:
        result_good.append(mass)

print(result_good)