#Loops
for x in range(0,100):
    print(x)

for x in range(0,100,2): # формат такой: (от, до, шаг)
    print(x)
    if x == 50:
        break # несмотря на то, что до =100, достигнув 50 цикл прервётся.
print("===============End of File===================================")
x = 0
while True:
    print(x)
    x = x + 1
    if x == 50:
        break

#********************************************************************************************

#Massivy

cities = ["York", "Kiev", "London", "Kiel", "Toronto"]
print(cities) # распечатать всё содержание масства

print(len(cities)) # вывести количество элементов в массиве
print(cities[3]) # распечатать 3-й элемент массива. Отсчёт элементов начинается с нуля
print(cities[-3]) # распечатать 3-й элемент массива с конца

cities [2] = "Odessa" # London заменится на Odessa
print(cities)

cities.append("Lvov") # append - добавляет новый элемент в конец массива
print(cities)

cities.insert(2, "Dnepr") # insert(куда добавить, что добавить) - в данном случае добавляет Dnepr на вторую позицию
print(cities)

del cities[-1] # убиваем в массиве элемент по указанной позиции (в данном случае 1-й с конца)
print(cities)

cities.remove("York") # убиваем в массиве элемент с указанным именем
print(cities)

deleted_city = cities.pop()# в скобках указываем индекс массива. Если его нет, то переменной присваевается последний
#элемент массива, который удаляется. Можно из массива выводить элементы в переменные
print("Deleted city is: " + deleted_city)
print(cities)

cities.sort() # упорядовачивание элементов массива по алфавиту или по возрастанию значений
print(cities)
cities.sort(reverse=True) # упорядовачивание элементов массива по алфавиту в обратном порядке или по уменьшению значений
print(cities)
#cities.sort(reverse=True) - это тоже самое, что и cities.reverse()

cars = ["BMW", "vw", "Skoda", "DAF", "Volvo"]
for x in cars:
    print(x.upper()) # берём каждый элемент массива и выводим на экран, изменяя буквы названия на заглавные

#for x in range(0, 10):   это тоже самое, что       my_number_list = list(range(0, 10))
#    print(x)                                       print(my_number_list)
# основная разница в том, что через for выводятся числа по одному в строке, а через list(range) числа выводятся внутри
# массива, что позволяет создавать массив автоматически из заданного количества элементов.

my_number_list = list(range(0, 10))
print(my_number_list)

for x in my_number_list:
    x = x * 2
    print(x)

print("Max number is: " + str(max(my_number_list))) # выведется на экран элемент массива с максимальным значением
print("Min number is: " + str(min(my_number_list))) # выведется на экран элемент массива с минимальным значением
print("Sum of all number is: " + str(sum(my_number_list))) # выведется на экран сумма всех элементов массива

mycars = cars[1:3] # создаёт новый массив из элементов существующего. формат [с какого элемента начинать, сколько
# элементов после него добавить, т.е. начать с первого элемента и до третьего элемента, не включая последний (будут 1-й,
# 2-й) и всё.]
print(mycars)
# по аналогии cars[:4] - с начала и до 4-го элемента массива
# cars {-3, -1} - с третьего элемента с конца и до последнего

mine = cars[:] # создаёт независимую копию массива, в которой не будут отопражаться изменения в источнике (cars)
print(cars)
print(mine)





