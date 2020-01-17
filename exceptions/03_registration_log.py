# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


class Error(Exception):
    """Base class for other user-defined exceptions"""
    pass


class NotEmailError(Error):
    def __str__(self):
        return 'Указан некорректный email'


class NotNameError(Error):
    def __str__(self):
        return 'Указано некорректное имя'


def parse_log(input_line):
    name, email, age = input_line.split(' ')
    age = int(age)
    if not name.isalpha():
        raise NotNameError('Указано некорректное имя')
    elif not 10 < age < 99:
        raise ValueError('Указан некорректный возраст')
    elif not ('@' in email and '.' in email[email.index('@'):]):
        raise NotEmailError('Указан некорректный email')
    else:
        return name, email, age


with open('./registrations.txt', 'r') as ff:
    for num, line in enumerate(ff):
        try:
            parse_log(line)
        except Exception as exc:
            with open('registrations_bad.log', 'a+') as file2:
                file2.write(f'Это некорректно: {line}, строка {num + 1}, {exc}\n')
        else:
            with open('registrations_good.log', 'a+') as file:
                file.write(line)

# зачет!
