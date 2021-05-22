#Задание 1
list = ["sun", 12, 12.3, None, True]
for element in list:
    print(type(element))

# Задание 2
n = []
num = int(input())
for i in range(num):
    new_element = int(input())
    n.append(new_element)
print(n)

i = 1
while i < len(n):
    print(n[i], n[i - 1])
    n[i], n[i - 1] = n[i - 1], n[i]
    print(n)
    i += 2

# Задание 3

season = {'Winter': (1, 2, 12),
          'Spring': (3, 4, 5),
          'Summer': (6, 7, 8),
          'Autumn': (9, 10, 11)}
num = int(input("Введите месяц:"))
for element in season:
    if num in season[element]:
        print(element)

#Задание 4
s = input()
ss = s.split()
print(ss)
for i, v in enumerate(ss):
    print(i, v)

#Задание 5
my_list = [7, 5, 3, 3, 2]
n = int(input())
my_list.append(n)
my_list1 = my_list.sort()
my_list1 = my_list.reverse()
print(my_list)