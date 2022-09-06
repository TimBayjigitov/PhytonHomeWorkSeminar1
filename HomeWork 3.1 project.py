# 3. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Вариант решения №2 для всех значений предикатов
x = 0
y = 0
z = 0
check = not (x or y or z) == (not x and not y and not z)
print(f'Проверка истинности условия ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z с данными значениями X = {x}, Y = {y}, Z = {z} -> {check}')
x = 0
y = 0
z = 1
check = not (x or y or z) == (not x and not y and not z)
print(f'Проверка истинности условия ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z с данными значениями X = {x}, Y = {y}, Z = {z} -> {check}')
x = 0
y = 1
z = 0
check = not (x or y or z) == (not x and not y and not z)
print(f'Проверка истинности условия ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z с данными значениями X = {x}, Y = {y}, Z = {z} -> {check}')
x = 0
y = 1
z = 1
check = not (x or y or z) == (not x and not y and not z)
print(f'Проверка истинности условия ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z с данными значениями X = {x}, Y = {y}, Z = {z} -> {check}')
x = 1
y = 0
z = 0
check = not (x or y or z) == (not x and not y and not z)
print(f'Проверка истинности условия ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z с данными значениями X = {x}, Y = {y}, Z = {z} -> {check}')
x = 1
y = 0
z = 1
check = not (x or y or z) == (not x and not y and not z)
print(f'Проверка истинности условия ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z с данными значениями X = {x}, Y = {y}, Z = {z} -> {check}')
x = 1
y = 1
z = 0
check = not (x or y or z) == (not x and not y and not z)
print(f'Проверка истинности условия ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z с данными значениями X = {x}, Y = {y}, Z = {z} -> {check}')
x = 1
y = 1
z = 1
check = not (x or y or z) == (not x and not y and not z)
print(f'Проверка истинности условия ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z с данными значениями X = {x}, Y = {y}, Z = {z} -> {check}')