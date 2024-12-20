# main.py - стартовый модуль проекта
 
# Импорты из модуля
from func import clean_phone_numbers

# Функция запуска импортированных функций
def main():
    input_file = 'phone_numbers.xlsx'  # Укажите путь к вашему файлу
    output_file = 'cleaned_phones.xlsx'  # Имя выходного файла
    clean_phone_numbers(input_file, output_file) 
    
# Инициализационный скрипт
if __name__ == "__main__":
    main()