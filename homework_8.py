""" Задача 1-10 - оберіть декілька домашніх завдань та покрийте їх не менш ніж 10 тестами.
Код закомітьте в гіт, надайте посилання.
На оцінку впливає як якість тестів так і розмір тестового покриття.
Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.
"""
import unittest
from notes import *

class HomeworksTesting(unittest.TestCase):

    def test_sum_numbers(self):
        """"The sum of numbers 2 and 21"""
        actual_result = sum_numbers(2, 21)
        expected_result = 23
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
