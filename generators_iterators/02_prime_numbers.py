# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:
    def __init__(self, n):
        self.n = n  # диапазон
        self.number = 1
        self.prime_numbers = []

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.number > self.n:
            raise StopIteration()
        else:
            for self.number in range(self.number, self.n + 1):
                if all(self.number % prime != 0 for prime in self.prime_numbers):
                    self.prime_numbers.append(self.number)
                    return self.number


prime_number_iterator = PrimeNumbers(n=10000)
for el in prime_number_iterator:
    print(el)


# после подтверждения части 1 преподователем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    number = 2
    for number in range(number, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


for el in prime_numbers_generator(n=10000):
    print(el)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.

# ===1===

def is_lucky(n):
    numbers = str(n)
    numbers = [int(i) for i in numbers]
    if len(numbers) % 2 == 0:
        val = len(numbers) // 2
        if sum(numbers[:val]) == sum(numbers[val:]):
            return True
    else:
        val = len(numbers) // 2
        if sum(numbers[:val]) == sum(numbers[(val + 1):]):
            return True


result = filter(is_lucky, get_prime_numbers(10000))
print(list(result))


# ===2===

def is_palindrome(n):
    rev_s = ''.join(reversed(str(n)))
    if str(n)[:len(str(n)) // 2] == rev_s[:len(rev_s) // 2]:
        return True


result = filter(is_palindrome, get_prime_numbers(10000))
print(list(result))


# ===3=== Happy number https://en.wikipedia.org/wiki/Happy_number


def happy(n):
    past = set()
    while n != 1:
        n = sum(int(i) ** 2 for i in str(n))
        if n in past:
            return False
        past.add(n)
    return True


result = filter(happy, get_prime_numbers(10000))
print(list(result))

# Простые счастливые палиндромные числа
result = filter(is_lucky, filter(is_palindrome, get_prime_numbers(1000)))
print(list(result))

