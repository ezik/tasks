# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

from datetime import datetime


class LogAnalyzer:
    def __init__(self, file_name, results_file):
        self.file_name = file_name
        self.results_file = results_file
        self.sorting_res_list = []
        self.stats = {}

    @property
    def format_string(self):
        raise NotImplementedError

    def extract_lines(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            for line in file:
                if 'NOK' in line:
                    datetime_obj = datetime.strptime(line, "[%Y-%m-%d %H:%M:%S.%f] NOK\n")
                    formatted_datetime_obj = datetime_obj.strftime(self.format_string)
                    self.sorting_res_list.append(str(formatted_datetime_obj))

    def calculate_result(self):
        for el in self.sorting_res_list:
            if el in self.stats:
                self.stats[el] += 1
            else:
                self.stats[el] = 1

    def write_to_file(self):
        with open(self.results_file, 'w', encoding='utf-8') as results_file:
            for key, value in self.stats.items():
                results_file.write('[{}] {} \n'.format(key, value))


class MinuteLogAnalyzer(LogAnalyzer):
    format_string = "%Y-%m-%d %H:%M"


class HourLogAnalyzer(LogAnalyzer):
    format_string = "%Y-%m-%d %H"


class MonthLogAnalyzer(LogAnalyzer):
    format_string = "%Y-%m"


class YearLogAnalyzer(LogAnalyzer):
    format_string = "%Y"


by_minute = MinuteLogAnalyzer(file_name='events.txt', results_file='stat_by_min.txt')
by_minute.extract_lines()
by_minute.calculate_result()
by_minute.write_to_file()

by_hour = HourLogAnalyzer(file_name='events.txt', results_file='stat_by_hour.txt')
by_hour.extract_lines()
by_hour.calculate_result()
by_hour.write_to_file()

by_month = MonthLogAnalyzer(file_name='events.txt', results_file='stat_by_month.txt')
by_month.extract_lines()
by_month.calculate_result()
by_month.write_to_file()

by_year = YearLogAnalyzer(file_name='events.txt', results_file='stat_by_year.txt')
by_year.extract_lines()
by_year.calculate_result()
by_year.write_to_file()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

# Спасибо за разъяснения, стало понятней
# зачет!
