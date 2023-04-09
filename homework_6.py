# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_numbers(first, second):
    return first + second

a = 10
b = 13
print("The total sum of two numbers:", sum_numbers(a, b))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел."""

def arithmetic_average(list_numbers):
    return sum(list_numbers) / len(list_numbers)

list_numbers = [1, 2, 3, 4]
print("The arithmetic average for list of numbers:", arithmetic_average(list_numbers))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_line(line):
    return line[::-1]

line = "Hello!!!!"
print("The line in reverse order:", reverse_line(line))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(list_of_words):
    return max(list_of_words, key=len)

list_of_words = ['Hello', 'world!', 'Thats', 'all.']
print("The longest word from the list:", longest_word(list_of_words))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    index = str1.find(str2)
    return index

str1 = "Hello, world!"
str2 = "world"

print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
#1. Знайдіть і поверніть всі унікальні елементи в списку

def find_unique_elements_in_list(list):
    new_list = set(list)
    return new_list

elements = [3, 1, 4, 5, 2, 5, 10]
print("All unique elements from list :", find_unique_elements_in_list(elements))

#2. Перевірте, чи є в списку дублікати

def check_dublicates_in_list(list):
    new_big_list = set(list)
    return len(new_big_list) == len(big_list)

big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
print("Do we have dublicated in the list?:", check_dublicates_in_list(big_list))


#3. Обчисліть суму елементів двох множин, які не є спільними
def sum_elements_not_common_sets(first_set, second_set):
    new_set = first_set ^ second_set
    total_sum = 0
    for i in new_set:
        total_sum += i
    return total_sum

set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}

print("The total sum of elements from two lists that are not common:", sum_elements_not_common_sets(set_1, set_2))


#4. Потрібно знайти список квадратів парних чисел зі списку.
def find_squares_of_paired_numbers(list_elements):
    result = [i ** 2 for i in list_elements if i % 2 == 0 ]
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The list of squares of even numbers from a list:", find_squares_of_paired_numbers(numbers))
