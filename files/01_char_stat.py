# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

from operator import itemgetter
import os
from os import path
import zipfile


class CharCounter:
    filename = ''

    def __init__(self, zip_file_name):
        self.zip_file_name = zip_file_name
        self.stat = {}
        self.stat_list = []
        self.total = 0

    def extract_file(self):
        if path.exists('voyna-i-mir.txt'):
            self.filename = 'voyna-i-mir.txt'
        else:
            zfile = zipfile.ZipFile(self.zip_file_name, 'r')
            for filename in zfile.namelist():
                self.filename = zfile.extract(filename)
                if os.path.isfile(self.filename):
                    return
                else:
                    print('No files found in {}'.format(self.zip_file_name))

    def collect_stats(self):
        try:
            with open(self.filename, 'r', encoding='cp1251') as file:
                for line in file:
                    for char in line:
                        if char.isalpha():
                            if char in self.stat.keys():
                                self.stat[char] += 1
                            else:
                                self.stat[char] = 1
            self.stat_list = [(key, value) for key, value in self.stat.items()]
        except FileNotFoundError:
            print('No file given for stat calculation in {}'.format(self.filename))

    def sort_stat_list(self, key=itemgetter(0), reverse=False):
        self.stat_list.sort(key=key, reverse=reverse)

    def sum_total(self):
        for el in self.stat_list:
            key, value = el
            self.total += value

    def print_results(self):
        print('+{:-^21}+'.format('+'))
        for el in self.stat_list:
            key, value = el
            print('|{key:^10}|{value:^10}|'.format(key=key, value=value))
        print('+{:-^21}+'.format('+'))
        print('|{key:^10}|{value:^10}|'.format(key='итого', value=self.total))
        print('+{:-^21}+'.format('+'))


# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828


char_counter = CharCounter(zip_file_name='./python_snippets/voyna-i-mir.txt.zip')
char_counter.extract_file()
char_counter.collect_stats()
char_counter.sum_total()

# Sort by "по частоте - по убыванию"
char_counter.sort_stat_list(key=itemgetter(1), reverse=True)
char_counter.print_results()

# Sort by "по частоте по возрастанию"
char_counter.sort_stat_list(key=itemgetter(1))
char_counter.print_results()

# Sort by "по алфавиту по возрастанию"
char_counter.sort_stat_list(key=itemgetter(0))
char_counter.print_results()

# Sort by "по алфавиту по убыванию"
char_counter.sort_stat_list(key=itemgetter(0), reverse=True)
char_counter.print_results()

# зачет!
