import os
import random
import string

def generate_uuid(length):
    # �������� ��������� �����
    random_bytes = os.urandom(16)
    
    # ����������� ����� � ������ ������������������ �������������
    uuid_hex = ''.join(f'{b:02x}' for b in random_bytes)
    
    # ���������� ���� ������ � ����������� ������
    return uuid_hex[:length]