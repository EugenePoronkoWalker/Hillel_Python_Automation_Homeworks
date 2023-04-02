small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list

new_list = set(small_list)
print("All unique elements in 'smail_list' list:", new_list)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list

amount_of_elements = len(small_list)
sum_elements = sum(small_list)
average_arithmetic = sum_elements / amount_of_elements
print("The average arithmetic of all items in the 'small_list' list", average_arithmetic)


# task 3. Перевірте, чи є в списку big_list дублікати

new_big_list = set(big_list)
print(len(new_big_list) == len(big_list))


base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict

new_dict = {}
biggest_value = 0
for key, value in add_dict.items():
    if biggest_value <= int(value):
        biggest_value = value
        save_key = key
new_dict.update({save_key:biggest_value})
print("The key with the biggest value in 'add_dict' dictionary:", new_dict)

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику

new_base_dict = {}
for key, value in base_dict.items():
    new_base_dict.update({value:key})
print("The new dictionary with swapped key and value:", new_base_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то об'єднайте (str) або додайте їх значення (int)

sum_dict = {}
sum_dict.update(base_dict)

for key, value in add_dict.items():
    if key in sum_dict:
        value += sum_dict[key]
    sum_dict.update({key:value})
print("Dictionary with merged two dictionaries and sum of values of the matching key:", sum_dict)

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"

new_set = set(line)
print("The set with unique elements:", new_set)

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}

new_set = set_1 ^ set_2

total_sum = 0
for i in new_set:
    total_sum += i
print("The total sum of elements from two lists that are not common:", total_sum)

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

first_list = [1, 2, 5, 6, 7, 10, 12, 15]
second_list = [3, 5, 12, -3, 10, 4, 13]

from_list_to_set = set(second_list) ^ set(first_list)
print("The set with unique elements from two lists:", from_list_to_set)


person_list = [('Boby', 19), ('Alice', 25) , ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

person_dict = {'10-19': [], '20-29': [], '30-39': [], '40-49': []}
for k, v in person_list:
    if v >= 10 and v <= 19:
        person_dict['10-19'].append(k)
    elif v >= 20 and v <= 29:
        person_dict['20-29'].append(k)
    elif v >= 30 and v <= 39:
        person_dict['30-39'].append(k)
    elif v >= 40 and v <= 49:
        person_dict['40-49'].append(k)
print("The new sorted dictionary:", person_dict)
