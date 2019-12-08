# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

from datetime import datetime


def calc_failed_events(log_fh):
    with open(log_fh, 'r') as f:
        previous_date_obj = datetime.fromtimestamp(1)
        i = 0
        for line in f:
            if 'NOK' in line:
                current_date_obj = datetime.strptime(line, "[%Y-%m-%d %H:%M:%S.%f] NOK\n") \
                    .replace(microsecond=0, second=0)
                if current_date_obj.time() != previous_date_obj.time():
                    previous_date_str = previous_date_obj.strftime("%Y-%m-%d %H:%M")
                    if i > 0:
                        yield previous_date_str, i
                    previous_date_obj = current_date_obj
                    i = 1
                else:
                    i += 1


grouped_events = calc_failed_events('./events.txt')
for el in grouped_events:
    print(el)

