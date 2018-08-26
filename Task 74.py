"""
Task 74

Дробь x/n называется правильной несократимой, если выполнены условия:
1.0 < X < N
НОД(X,N) = 1,

где N - натуральное число, где N<10**6

Необходимо вывести количество правильных несократимых дробей со знаменателем N.
Например:
N = 11, Result = 10
N = 12, Result = 4
N = 17, Result = 16

"""

'''
идея: ищем все простые делители N и выкидываем все числа до числа N,
которые делятся хотя бы на один из них
'''


def dividers_number(N):
    res = N - 1  # количество всех дробей со знаменателем N
    for i in range(2, N // 2 + 1):
        if N % i == 0:  # проверка делимости без остатка числа N на это число
            count = 0
            for j in range(1, int(i ** 0.5) + 1):  # простое ли это число
                if i % j == 0:
                    count += 1
            if count == 1:
                res -= res // i  # если простое, то выкидываем все числа до N, делящиеся на это число
    return res


assert (dividers_number(2) == 1)
assert (dividers_number(3) == 2)
assert (dividers_number(18) == 6)
assert (dividers_number(11) == 10)
assert (dividers_number(12) == 4)
assert (dividers_number(41) == 40)
assert (dividers_number(99) == 60)
