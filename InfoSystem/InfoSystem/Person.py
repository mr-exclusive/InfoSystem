# -*- coding: cp1251 -*-

# ����� ������� (��������)
from datetime import date
from TypeOfGenders import TypeOfGenders

class Person:

    # ���
    first_name: str
       
    # �������
    last_name: str
       
    # ��������
    middle_name: str
        
    # ���� �������� � ��������� datetime
    date_of_birth: date

    # ���
    gender: TypeOfGenders

    # ��� "�����������" ���������� ������. 
    # ����� ��������� �������� ������ �������� �� �������� ����
    # self - ��� �������� �����, ����������� �� ��, ��� ��� �� ������ �������,
    # � ������� ������ ��� ���������� ������
    def __init__(self, firstName:str, lastName:str, middleName:str, dob:date, gender:TypeOfGenders):

        self.first_name = firstName

        self.last_name = lastName

        self.middle_name = middleName

        self.date_of_birth = dob

        self.gender = gender


    # ������� ������������� ������� � ���� ������ (����� �� �������)
    def to_string(self):

        return self.last_name + ' ' + self.first_name + ' ' + self.middle_name + ' (' + \
            str(self.date_of_birth.day).zfill(2) + '.' + \
            str(self.date_of_birth.month).zfill(2) + '.' + \
            str(self.date_of_birth.year).zfill(4) + ')'


