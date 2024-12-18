# func.py - модуль с функциями
import pandas as pd
import re

# Функция для очистки номера телефона
def clean_phone_number(phone):
    return re.sub(r'\D', '', str(phone)) # Удаляем все, кроме цифр

# Функция для обработки всех номеров в файле
def clean_phone_numbers(input_file, output_file):
    df = pd.read_excel(input_file)  # Загружаем Excel файл
    df['cleaned_phone'] = df['phone_number'].apply(clean_phone_number)  # Обрабатываем столбец 'phone'
    df.to_excel(output_file, index=False)  # Сохраняем результат в новый файл