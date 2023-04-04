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
