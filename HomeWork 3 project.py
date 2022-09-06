#3. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Вариант решения №1 через random
from random  import randint
x = randint(0, 1)
y = randint(0, 1)
z = randint(0, 1)
check = not (x or y or z) == (not x and not y and not z)
print(f'Проверка истинности условия ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z с данными значениями X = {x}, Y = {y}, Z = {z} -> {check} ')