# -*- coding: cp1251 -*-

# ����� ��� ������ � ������� � ������/�������

from typing import Tuple


class IO_system:

    def read_statement(file_name:str):

        # ������� ������ ����� �������� ����
        # �������� � ������ ������ ��������� �� DataManager
        # �� ����� ��� ����� ��� ������ ���� � ����
        # �� ������ ������ ���� (persons, position, departments, employees)

        return

    def write_statement(statement:Tuple):

        # ������� ������ ��������� ���� ������ � ����
        # �������� � ����� ������ ��������� �� DataManager
        # �� ����� ������ ���� (persons, position, departments, employees)

        return
    

    def read_index(message:str, minIndex:int, maxIndex:int):

        index = minIndex - 1

        while index < minIndex or index > maxIndex:

            index = int(input(message)) - 1

        return index
    

    def print_a_list_with_indexes(list_to_print):

        index = 1

        for item in list_to_print:

            print(str(index) + '. ' + item.to_string())

            index += 1

    pass


