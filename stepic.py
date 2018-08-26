# fib = lambda x: 1 if x <= 2 else fib(x - 1) + fib(x - 2)
# print(fib(31))
# sum = 0
# for i in range(int(input())):
#    sum += int(input())
# print(sum)

# print(42 / (4 + 2 * (-2)))
# print(2014.0 ** 14)
# print(1.2345e-3)
# print(9**19 - int(float(9**19)))

# x = int(input())
# h = int(input())
# m = int(input())
# H = (x // 60 + h) + (x - ((x // 60) * 60) + m) // 60
# M = (((x - (x // 60) * 60) + m) % 60)
# print(H)
# print(M)

# a = True
# b = False
# print(a and b or not a and not b)

# A = int(input())
# B = int(input())
# H = int(input())
# if A <= H <= B:
#    print("Это нормально")
# elif H > B:
#    print("Пересып")
# else:
#    print("Недосып")

# a = float(input())
# b = float(input())
# c = float(input())
# p = (a + b + c) / 2
# print((p * (p - a) * (p - b) * (p - c)) ** 0.5)

# x = float(input())
# if -15 < x <= 12 or 14 < x < 17 or 19 <= x:
#    print(True)
# else:
#    print(False)

# a = float(input())
# b = float(input())
# mode = input()
# if mode == '*':
#    print(a * b)
# elif mode == '-':
#    print(a - b)
# elif mode == '+':
#    print(a + b)
# elif mode == '/':
#    if b == 0:
#        print("Деление на 0!")
#    else:
#        print(a / b)
# elif mode == 'mod':
#    if b == 0:
#        print("Деление на 0!")
#    else:
#        print(a % b)
# elif mode == 'pow':
#    print(a ** b)
# elif mode == 'div':
#    if b == 0:
#        print("Деление на 0!")
#    else:
#        print(a // b)
# else:
#    print('mode выбран неправильно')

# forma = input()
# if forma == 'треугольник':
#    a = float(input())
#    b = float(input())
#    c = float(input())
#    p = (a + b + c) / 2
#    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
# elif forma == 'прямоугольник':
#    print(float(input()) * float(input()))
# elif forma == 'круг':
#    print(3.14 * float(input())**2)
# else:
#    print("Такой фигуры нет")
# a = []
# for i in range(3):
#    a.append(int(input()))
# a.sort()
# print(max(a))
# print(min(a))
# print(a[1])
# number = int(input())
#
# if number <= 10:
#    if number == 0 or number > 4:
#        print(str(number), 'программистов')
#    elif number == 1:
#        print(str(number), 'программист')
#    else:
#        print(str(number), 'программиста')
# elif 11 <= number <= 20 or 111 <= number <= 120 or 211 <= number <= 220 or 311 <= number <= 320 or 411 <= number <= 420 or 511 <= number <= 520 or 611 <= number <= 620 or 711 <= number <= 720 or 811 <= number <= 820 or 911 <= number <= 920:
#    print(str(number), 'программистов')
# elif number >= 21:
#    if number % 10 == 0 or number % 10 > 4:
#        print(str(number), 'программистов')
#    elif number % 10 == 1:
#        print(str(number), 'программист')
#    elif 2 <= number % 10 <= 4:
#        print(str(number), 'программиста')

# bilet = int(input())
# if ((bilet // 100000) + (bilet - (bilet // 100000) * 100000) // 10000 + (bilet // 1000) % 10) == (
#        (bilet % 1000) // 100 + (bilet % 100) // 10 + (bilet % 10)):
#    print("Счастливый")
# else:
#    print("Обычный")
# s = 0
# t = True
# while t:
#    i = int(input())
#    if i == 0:
#        t = False
#    else:
#        s += i
# print(s)

# while True:
#    n = int(input())
#    if n < 10:
#        continue
#    elif n > 100:
#        break
#    else:
#        print(n)
