# -*- coding: cp1251 -*-

# ������ ���� ��������� ��������� ������ ��������� 

# �����, � ������� ����� ������� ������ � �������.
# ����� �������� ��� ������ � ����� � ��������, ��������� ���������� � ������.
# ����� ����������, �������� �����, ����������, �������, ������ � ������ �������� �������� 
# ���� ������ � ���� � ���������� ������

from datetime import date
from Position import Position
from TypeOfPositions import TypeOfPositions
from TypeOfLevels import TypeOfLevels
from TypeOfGenders import TypeOfGenders
from TypeOfDepartments import TypeOfDepartments
from Person import Person
from IO_system import IO_system

class DataManager:
    
    positions = [] # ������ ����������. �������� ������� - ���������� ������ Position

    persons = [] # ������ �����. �������� ������� - ���������� ������ Person

    employees = [] # �����������.  �������� ������� - ������ (PersonID, PositionID, TypeOfDepartment)


    # �������� ��������. ��� �� ������� �� �����-�� ���������� � ������� ���������, � ������������ ���������� �������
    # ����������� ������ DataManager, ������ � ������� ����� ������� �� InfoSyste
    def init_system(self):

        # ������� ����� �������, ���� ������ � ��������� ��� ��� ������
        
        self.positions = []

        self.positions.append(Position(200.0,TypeOfPositions.boss,TypeOfLevels.senior))
        
        self.positions.append(Position(50.0,TypeOfPositions.manager, TypeOfLevels.middle))
        
        self.positions.append(Position(600.0,TypeOfPositions.cleaner, TypeOfLevels.senior))



        self.persons = []

        self.persons.append(Person('����', '��������', '���������', date(1988, 1, 15), TypeOfGenders.male))

        self.persons.append(Person('����', '�����', '������', date(1993, 5, 28), TypeOfGenders.male))


        self.employees = []

        self.employees.append((0, 0, TypeOfDepartments.head))
        
        self.employees.append((2, 1, TypeOfDepartments.stuff))

        # ������ �� ����� �������� �������� � ������� ������� (�������� ��� � �������)
        # ����� ��������� ���������. ����� ��� ������������ ������� �������� �� ������ (���� ����� ������ �� ��������)  � ��

        return

    # ������� ��������� ��������. ��� �� ������ ���� �� �� ��� �����
    def add_person(self):

        print(' ������� ������ ��������:')

        # ���� ����� ����. ��� �������� �����

        self.persons.append(Person(
            input('���:'), 
            input('�������:'), 
            input('��������:'), 
            date(input('��� ��������:'), input('����� ��������:'), input('���� �������:')), 
            TypeOfGenders(input('�������� ���. ������� ���: 1 , ������� ���: 2'))))

        return

    # ������� ��������� ���������. �������������� ����� �������� ������� persons � �������� ������� position
    def add_employee(self):

        print(' ������� ������ ����������.')
                
        print(' �������� ���������� ��������:')

        # �������� ������� ��� ������, ������������ �� ���� ���� ������� ������� ����� ������� to_string() 
        IO_system.print_a_list_with_indexes(self.persons)

        person_index = IO_system.read_index(' ������� ����� ��������', 0, len(self.persons) - 1)

        
                
        print(' �������� ��������� ���������:')

        IO_system.print_a_list_with_indexes(self.positions)

        position_index = IO_system.read_index(' ������� ����� ����������', 0, len(self.positions) - 1)


                
        print(' �������� �����:')

        for dt in TypeOfDepartments:

            # �������� ��������� �������� �� ������������ TypeOfDepartments (��� � ���)
            print(str(dt.value) + ': ' + str(dt.name))

        availableDepartmentCodes = [e.value for e in TypeOfDepartments]

        selectedDepartment = -1

        while selectedDepartment not in availableDepartmentCodes:

            selectedDepartment = int(input(' ������� ��� ���������:'))



        # ��� ������ ��� ���������� ����������
        self.employees.append((person_index, position_index, TypeOfDepartments(selectedDepartment))) 

        return