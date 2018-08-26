# условные операторы

x = 25
if x == 25:
    print("!")
else:
    print("?")

# Словари

# Создаём словарь
#   (-----Item-----)
#   (key)    (value)

enemy = {
    "loc_x": 70,
    "loc_y": 50,
    "color": "green",
    "health": 100,
    "name": "Monster",
# внутри словаря может быть массив
# например, массив изображений, меняющийся в зависимости от каких-то условий
    "image" : ["image1.jpg", "image2.jpg","image3.jpg","image4.jpg",] # и далее через IF берём нужную картинку
}

print(enemy)  # печатаем всё содержимое

# печатаем выборочно параметры
print("Location X = " + str(enemy["loc_x"]))
print("Location Y = " + str(enemy["loc_y"]))
print("His name is = " + enemy["name"])

# добавляем ещё один параметер в словарь
enemy["range"] = "Admiral"
print(enemy)

# удаляем параметры из словаря
del enemy["range"]
print(enemy)

# вносим изменения в существующие параметры
enemy["loc_x"] = enemy["loc_x"] + 40
enemy["health"] = enemy["health"] - 30
if enemy["health"] < 80:
    enemy["color"] = "yellow"

print(enemy)
print(enemy.keys())
print(enemy.values())

# Сделаем массив из словарей (10 одинаковых - копирует первоначальный словарь, но копии зависят от источника)
all__enemies = []

for y in range (0, 10):
    all__enemies.append(enemy.copy())

# чтобы все данные были не в одну строчку при выводе, а в приличном виде, делаем
for enemy in all_enemies:
    print (enemy)

for enemy in all__enemies:
    print (enemy)