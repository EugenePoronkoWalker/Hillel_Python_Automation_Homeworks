# task 01 == Розділіть змінну так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
alice_in_wonderland = """Would you tell me, please, which way I ought to go from here?"\n
    "That depends a good deal on where you want to get to," said the Cat.\n
    "I don\'t much care where ——" said Alice.\n
    "Then it doesn\'t matter which way you go," said the Cat.\n
    "—— so long as I get somewhere," Alice added as an explanation.\n
    "Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."""


# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
area_of_black_sea = 436_402
area_of_azov_sea = 37_800
total_area = area_of_azov_sea + area_of_black_sea
print('Area of Black Sea and Azov Sea:', total_area, 'км2')

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_quantity = 375_291
first_and_second = 250_449
second_and_third = 222_950

quantity_in_first = total_quantity - second_and_third
quantity_in_third = total_quantity - first_and_second
quantity_in_second = total_quantity - (quantity_in_first + quantity_in_third)

print("Quantity on the first storage:", quantity_in_first,"\n"\
    "Quantity on the second storage:", quantity_in_second,"\n"\
    "Quantity on the third storage:", quantity_in_third)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
monthly_payment = 1179
amount_of_mounths = 18
for computer_price in range (1, (amount_of_mounths + 1)):
    computer_price *= monthly_payment
print("Computer costs:", computer_price)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print("Remainder of the division of numbers:", "\n", "a)", a,"\n","b)", b, "\n",\
    "c)", c, "\n","d)", d, "\n","e)", e, "\n","f)", f)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

big_pizza = 274 * 4
middle_pizza = 218 * 2
juice = 35 * 4
cake = 350 * 1
water = 21 * 3
total_sum = big_pizza + middle_pizza + juice + cake + water
print("Total sum:", total_sum)


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
amount_of_photos = 232
amount_on_one_page = 8
total_amount_pages = int(amount_of_photos / amount_on_one_page)
print("Total amount of required pages:", total_amount_pages)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

trip_distance = 1600
full_tank = 48
petrol_on_100_km = 9

#1) Скільки літрів бензину знадобиться для такої подорожі?

amount_petrol_for_trip = int((trip_distance / 100) * petrol_on_100_km)
print("Total amount of petrol for trip:", amount_petrol_for_trip)

#2) Скільки щонайменше разів родині необхідно заїхати на зап-
#равку під час цієї подорожі, кожного разу заправляючи повний бак?

amount_times_to_gas_station = int(amount_petrol_for_trip / full_tank)
print("Total amount of filling tank:", amount_times_to_gas_station)
