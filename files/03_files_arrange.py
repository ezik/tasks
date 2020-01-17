# -*- coding: utf-8 -*-

import os
import time
import shutil
import calendar
from zipfile import ZipFile
import datetime


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class BaseFileArranger:
    def __init__(self, base_file, destination_dir):
        self.base_file = base_file
        self.destination_dir = destination_dir

    def prepare_filenames_list(self):
        raise NotImplementedError

    def store_files_meta(self):
        raise NotImplementedError

    def get_base_files_path(self):
        base_file_path_list = []
        filenames_list = self.prepare_filenames_list()
        for dirpath, file in filenames_list:
            full_path = os.path.join(dirpath, file)
            base_file_path_list.append(full_path)
        return base_file_path_list

    def get_destination_files_path(self):
        destination_path_list = []
        for file_year, file_month in self.store_files_meta():
            new_file_path = os.path.join(self.destination_dir, file_year, file_month)
            destination_path_list.append(new_file_path)
        return destination_path_list

    def copy_files(self):
        for base_path, new_file_path in zip(self.get_base_files_path(), self.get_destination_files_path()):
            if not os.path.exists(new_file_path):
                os.makedirs(new_file_path)
            shutil.copy2(base_path, new_file_path)


class FileArranger(BaseFileArranger):
    def __init__(self, base_file, destination_dir):
        super().__init__(base_file, destination_dir)
        self.base_dir = base_file

    def prepare_filenames_list(self):
        filenames_list = []
        for dirpath, _, filenames in os.walk(self.base_dir):
            for file in filenames:
                filenames_list.append((dirpath, file))
        return filenames_list

    def store_files_meta(self):
        metadata_list = []
        for dirpath, file in self.prepare_filenames_list():
            full_path = os.path.join(dirpath, file)  # here we can get full path from file_list prepare
            secs = os.path.getmtime(full_path)
            file_time = time.gmtime(secs)
            file_year = str(file_time.tm_year)
            file_month = calendar.month_abbr[file_time.tm_mon]
            metadata_list.append((file_year, file_month))
        return metadata_list


file_arranger = FileArranger(base_file='./icons', destination_dir='./icons_by_year')
file_arranger.copy_files()


# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828


class ArchiveFileArranger(BaseFileArranger):
    def __init__(self, base_file, destination_dir):
        super().__init__(base_file, destination_dir)
        self.archive_name = base_file

    def prepare_filenames_list(self):
        files_info_list = []
        with ZipFile(self.archive_name, 'r') as zip_list:
            for fileinfo in zip_list.infolist():
                files_info_list.append(fileinfo)
        return files_info_list

    def store_files_meta(self):
        metadata_list = []
        for fileinfo in self.prepare_filenames_list():
            date_time_value = datetime.datetime(*fileinfo.date_time)
            year = str(date_time_value.year)
            month = calendar.month_abbr[date_time_value.month]
            metadata_list.append((year, month))
        return metadata_list

    def set_paths_for_temp_location(self):
        extracted_files_path_list = []
        with ZipFile(self.archive_name, 'r') as zip_list:
            for fileinfo, path in zip(zip_list.infolist(), self.get_destination_files_path()):
                extracted_file_path = zip_list.extract(member=fileinfo.filename, path=path)
                extracted_files_path_list.append(extracted_file_path)
        return extracted_files_path_list

    def copy_files(self):
        path_for_files_move = []
        for file_meta, fileinfo in zip(self.store_files_meta(), self.prepare_filenames_list()):
            file_year, file_month = file_meta
            path_for_file_move = os.path.join(self.destination_dir, file_year, file_month,
                                              os.path.basename(fileinfo.filename))
            path_for_files_move.append(path_for_file_move)

        for path_after_copy, path_after_move in zip(self.set_paths_for_temp_location(), path_for_files_move):
            if os.path.isfile(path_after_copy):
                shutil.move(path_after_copy, path_after_move)

    def clean_up(self):
        for dirpath, _, _ in os.walk(self.destination_dir):
            if not len(os.listdir(dirpath)):
                os.removedirs(dirpath)


archive_file_arranger = ArchiveFileArranger(base_file='./icons.zip', destination_dir='./icons_by_year')
archive_file_arranger.copy_files()
archive_file_arranger.clean_up()

# зачет!
