# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
from cmath import sqrt
x1 = int(input('Введите координаты 1й точки + enter: '))
y1 = int(input('Введите координаты 1й точки + enter: '))
x2 = int(input('Введите координаты 2й точки + enter: '))
y2 = int(input('Введите координаты 2й точки + enter: '))
print(f'Расстояние между ними в 2D пространстве при значениях 1-й точки - ({x1},{y1}) и 2-й точки - ({x2},{y2}) -> {round(sqrt((x2-x1)**2 + (y2-y1)**2).real, 2)}')


