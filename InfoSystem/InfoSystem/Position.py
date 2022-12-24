# -*- coding: cp1251 -*-

from TypeOfPositions import TypeOfPositions
from TypeOfLevels import TypeOfLevels

class Position:
    
    # ��������
    salary: float

    # ��� ����������
    position_type: TypeOfPositions

    # ������� ���������
    position_level: TypeOfLevels

    def __init__ (self, salary:float,position_type:TypeOfPositions, position_level:TypeOfLevels):

        self.salary = salary

        self.position_type = position_type

        self.position_level = position_level

    # ������� ������������� ��������� � ���� ������ (����� �� �������)
    def to_string(self):

        return str(self.position_level) + ' ' + str(self.position_type) + ' (' + str(self.salary) + ' ������)'
