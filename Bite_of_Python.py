age = 26
name = 'Swaroop'
sex = "man"
print('Возраст {} {} -- {} лет.'.format(sex, name, age))
print('Почему {} {} забавляется с этим Python?'.format(sex, name))

# в {} заключаюся значения тех переменных и в том порядке, в котором они обозначены после .format в скобках
print('{name} написал {book}'.format(name='Swaroop', book='A Byte of Python'))

# заполнить подчёркиваниями (_) с центровкой текста (^) по ширине 11:
print('{0:_^11}'.format('hello'))

# десятичное число (.) с точностью в 3 знака для плавающих:
print('{0:.3}'.format(1 / 3))

# Явное объединение строк
s = 'Это строка. \
 Это строка продолжается.'
print(s)
# Это даст результат:
# Это строка. Это строка продолжается. (то есть, \ обединит две строки в одну)

# Global и nonlocal переменные (попробовать запустить код попеременно комментируя переменные)
def func_outer():
    x = 2
    print('x равно', x)

    def func_inner():
        #        nonlocal x # будет использоваться переменная, определённая внутри метода
        global x # будет использоваться переменная, где х = 2 
        x = 5
        y = x + 2
        print(y)
    func_inner()
    print('Локальное x сменилось на ', x)


func_outer()
