# task 1
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""

alien_color = 'green'
if alien_color == 'green':
    print('The player has just earned 5 points')

# task 2
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""
alien_color = 'red'
if alien_color == 'green':
    print('The player has just earned 5 points')
else:
    print('The player has just earned 10 points')

# task 3
# task 4
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
+ напишіть цикл for що перебере і обробить всі значення списку alien_color
"""

alien_color = ['green', 'yellow', 'red']
for i in alien_color:
    if i == 'green':
        print('The player has just earned 5 points')
    elif i == 'red':
        print('The player has just earned 15 points')
    else:
        print('The player has just earned 10 points')


# task 5
""" Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""
pizza_topping = 'not_quit'
while pizza_topping != 'quit':
    pizza_topping = input("Enter the pizza toppings:")
    print('We will add this topping to the pizza:', pizza_topping)

# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр натурального числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть натуральне число: 12345
Сума цифр числа 12345: 15
"""
number = int(input("Enter a number:"))
sum_all_numbers = 0
while number > 0:
    sum_all_numbers += number % 10
    number = number // 10
print("The sum of all numbers:", sum_all_numbers)

# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""
sum_of_numbers = 0
while True:
    current_number = int(input("Enter a number:"))
    if current_number == 0:
        print('The sum of all entred numbers:', sum_of_numbers)
        break
    sum_of_numbers += current_number

# task 8
"""  З використанням циклу for реалізуйте гру "Вгадай число".
Початок програми написаний, гравець має 5 спроб відгадати випадкове число від 1 до 20,
яке було згенеровано за допомогою функції randint() модуля random.
У кожній спробі гравець вводить своє припущення, після чого програма повідомляє, чи
було припущення занадто великим або занадто малим, чи гравець вгадав число.
"""
import random
secret_number = random.randint(1, 20)
guesses = 0
max_guesses = 5
print("Вгадайте число від 1 до 20 за 5 спроб!")


for i in range (1, (max_guesses + 1)):
    guess = int(input("Enter a number: "))
    guesses += 1
    if guess < secret_number:
        print("Your number is lower than mine!")
    elif guess > secret_number:
        print("Your number is bigger than mine!")
    else:
        break
if guess == secret_number:
    print("Yes, You are right, this is my number!")
else:
    print("I'm sorry but you didn't guess!")

# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]

# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = ["Відповідь вставте сюди"]
print(result)  #  [4, 16, 36, 64, 100]
