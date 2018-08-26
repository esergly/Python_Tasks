# Решение квадратного уравнения
i = "!"
while i == "!":
    question = input("Желаете решить квадратное уравнение? (yes/no): ")

    if question == "yes":
        print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        discriminant = b ** 2 - 4 * a * c
        print("Дискриминант D = %.2f" % discriminant)

        if discriminant > 0:
            import math
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            print("x1 = %.2f \nx2 = %.2f" % (x1, x2))

        elif discriminant == 0:
            x = -b / (2 * a)
            print("x = %.2f" % x)
        else:
            print("Корней нет")

    elif question == "no":
        print("Всего хорошего! ")
        i = "?"

    else:
        print("Попробуйте ввести ответ ещё раз... ")

# Определение существования треугольника
i = "+"
while i == "+":
    question2 = input("Желаете исследовать треугольник? (yes/no): ")
    if question2 == "yes":
        print("Введите стороны проверяемого треугольника: ")
        x = float(input("сторона a = "))
        y = float(input("сторона b = "))
        z = float(input("сторона c = "))
        if x + y > z and y + z > x and x + z > y:
            print("Такой треугольник существует")
        else:
            print("Такой треугольник не существует")

    elif question2 == "no":
        print("Всего хорошего! ")
        i = "?"

    else:
        print("Попробуйте ввести ответ ещё раз... ")

# Определение координат четверти плоскости
i = "."
while i == ".":
    question3 = input("Желаете исследовать треугольник? (yes/no): ")
    if question3 == "yes":
        print("Введите стороны проверяемого треугольника: ")
        x = float(input("сторона a = "))
        y = float(input("сторона b = "))
        z = float(input("сторона c = "))
        if x + y > z and y + z > x and x + z > y:
            print("Такой треугольник существует")
        else:
            print("Такой треугольник не существует")

    elif question3 == "no":
        print("Всего хорошего! ")
        i = "?"

    else:
        print("Попробуйте ввести ответ ещё раз... ")