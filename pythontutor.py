words, counter = {}, {}
line, result = [], []
for i in range(int(input())):
    line.append(input().split(" "))
for i in range(len(line)):
    for j in range(2, len(line[i])):
        words[line[i][j]] = line[i][0]
temp = line.copy()
line = []
for key in words:
    line.append(key)
line = sorted(list(line))
result = line.copy()
for i in range(len(line)):
    for j in range(len(line[i])):
        if "," in line[i][j]:
            result[i] = line[i][:j]
print(counter)
print(temp)
print(len(result))
test = []
for i in range(len(line)):
    for h in range(len(temp)):
        for j in range(len(temp[h])):
            if str(result[i]) in temp[h][j]:
                test.append(str(temp[h][0]) + ',')
    print(str(result[i]) + " - " + str(test))
    print(str(result[i]) + " - " + words[str(line[i])])








"""
3
apple - malum, pomum, popula
fruit - baca, bacca, popum
punishment - malum, multa

****************************************
7
baca - fruit
bacca - fruit
malum - apple, punishment
multa - punishment
pomum - apple
popula - apple
popum - fruit
"""
