"""
Task 78

Цифровой корень натурального числа — это цифра, полученная в результате итеративного процесса суммирования цифр, на каждой итерации которого для подсчета суммы цифр берут результат, полученный на предыдущей итерации. Этот процесс повторяется до тех пор, пока не будет получена одна цифра.

Необходимо составить программу нахождения цифрового корня натурального числа.

Входные данные: N - натуральное число, где 0 <= N <= 10^9
Вывод: цифровой корень числа N

Пример:
Number = 65536
В итоге получаем: 6+5+5+3+6=25 => 2+5=7
Выводим полученный результат:
DigitalRoot = 7

"""
'''
Идея простая: получаем вводимое число, разбираем его на цифры в виде элементов массива, складываем их и 
получаем число, состоящее из не более чем 2-х цифр. Это согласно условию (N <=10^9). 
Потом это число ещё раз прогоняем через функцию складывания элементов массива и получаем конечный результат.
'''


# Первый вариант решения
def digital_root(number):
    number_str = list(number)  # разбираем строчку с введённым числом на отдельные цифры
    my_list = []  # создаём массив для суммирования его будущих элементов
    for digit in number_str:
        my_list.append(int(digit))  # заполняем масcив поэлементно полученными цифрами
    return str(sum(element for element in my_list))


# Второй вариант решения (http://codeforces.com/blog/entry/18286)
def digital_root_nice(number):
    return str(1 + ((number - 1) % 9))


number = input("Введите натуральное число: \n")  # запрашиваем натуральное число для расчётов
# выводим полученный результат
print(digital_root(digital_root(number)))
print(digital_root_nice(int(number)))