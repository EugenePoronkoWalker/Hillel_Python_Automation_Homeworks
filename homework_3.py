adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.split()
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
amount_of_letter_h = 0
for symbol in adwentures_of_tom_sawer:
    if symbol == "h":
        amount_of_letter_h += 1
print("How many letters 'h' :", amount_of_letter_h)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
amount_of_uppercase_letters = 0
new_list_adwentures_of_tom_sawer = adwentures_of_tom_sawer.split()
for symbol in new_list_adwentures_of_tom_sawer:
    if symbol == symbol.title():
        amount_of_uppercase_letters += 1
print("How many words with capital letters:", amount_of_uppercase_letters)


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_place_Tom_word_in_text = adwentures_of_tom_sawer.find("Tom")
print("Position on which 'Tom' is the second time:", adwentures_of_tom_sawer.find("Tom", first_place_Tom_word_in_text + 1))


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("Fourth sentence in lower case:", adwentures_of_tom_sawer_sentences[3].lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
counter = 0
for words in adwentures_of_tom_sawer_sentences:
    if words.startswith("By the time") == True:
        counter += 1
print("How many sentences starts with words 'By the time':", counter)


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("How many words in the last sentence:", len(adwentures_of_tom_sawer_sentences[-1].split()))
