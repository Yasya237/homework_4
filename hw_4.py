#1) У вас є список my_list із значеннями типу int.
# Роздрукувати значення, які більше 100.
# Завдання виконати за допомогою циклу for.

my_list = [1, 35, 635, 100, 104]
results = []
for number in my_list:
    if number > 100:
        results.append(number)
        print(number)
#####################################################

# 2) У вас є список my_list зі значеннями типу int і порожній список my_results.
# Додати my_results ті значення, які більше 100.
# Роздрукувати список my_results.
# Завдання виконати за допомогою циклу for.

my_list = [1, 35, 635, 100, 104]
my_results = []
for number in my_list:
    if number > 100:
        my_results.append(number)
print(my_results)
#####################################################

# 3) У вас є список my_list із значеннями типу str. Створити новий список до якого помістити
# елементи з my_list за таким правилом:
# Якщо строка стоїть на непарному місці my_list, то її замінити на обернену строку (Наприклад "qwe" на "ewq")
# Якщо на парному – залишити без зміни.
# Завдання зробити за допомогою циклу for та функції enumerate.

my_list = ["qwe","kva","candy","cake"]
my_results = []
for idx, word in enumerate(my_list):
    if idx % 2 != 0:
        my_results.append(word[::-1])
    else:
        my_results.append(word)
print(my_results)
#####################################################

# Ще один приклад для for – вкладені цикли (цикл у циклі).
my_string_1 = "12"
my_string_2 = "34"
for symb_1 in my_string_1:
    for symb_2 in my_string_2:
        print(symb_1 + symb_2)

#Результат:
"13" # перебираються всі елементи з my_string_2 для елемента "1" з my_string_1
"14"
"23" # перебираються всі елементи з my_string_2 для елемента "2" з my_string_1
"24"
#####################################################

# 4) У вас є рядок my_string = '0123456789'.
# Згенерувати цілі числа (тип int) від 0 до 99 і помістити в список.
# Завдання потрібно виконати ТІЛЬКИ через цикл у циклі (Див. Приклад вище) і зведення типів !!!
# Генерування через range або інші "фішки" я не зараховуватиму ))

my_string = '0123456789'
new_string ='0123456789'
numbers = []
for symb_1 in my_string:
    for symb_2 in new_string:
        numbers.append(int(symb_1 + symb_2))
print(numbers)
