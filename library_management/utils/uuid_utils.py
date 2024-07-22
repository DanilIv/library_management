import os
import random
import string

def generate_uuid(length):
    # Получаем случайные байты
    random_bytes = os.urandom(16)
    
    # Преобразуем байты в строку шестнадцатеричного представления
    uuid_hex = ''.join(f'{b:02x}' for b in random_bytes)
    
    # Возвращаем срез строки с необходимой длиной
    return uuid_hex[:length]