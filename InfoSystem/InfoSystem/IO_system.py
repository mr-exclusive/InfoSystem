
# Класс для работы с файлами и вводом/выводом
from enum import Enum
from typing import Tuple


class IO_system:

    def read_statement(self, file_name:str):

        # Функция чтения файла состяния базы
        # вызываем в начале работы программы из DataManager
        # На входе имя файла или полный путь к нему
        # На выходе кортеж типа (persons, position, departments, employees)

        return

    def write_statement(self, statement:Tuple):

        # Функция записи состояния базы данных в файл
        # вызываем в конце работы программы из DataManager
        # На входе кортеж типа (persons, position, departments, employees)

        return
    

    def read_index(self, message:str, minIndex:int, maxIndex:int):

        index = minIndex - 1

        while index < minIndex or index > maxIndex:

            index = int(input(message)) - 1

        return index
    

    def print_a_list_with_indexes(self, list_to_print):

        index = 1

        for item in list_to_print:

            print(str(index) + '. ' + item.to_string())

            index += 1

    def select_from_enum(self, something: Enum, msg: str):

        for some in something:
            print(f'{some.value}: {some.name}')

        available_codes = [i for i in something]

        selected_code = -1

        while selected_code not in available_codes:
            selected_code = int(input(msg))
        
        return something(selected_code)


    pass


