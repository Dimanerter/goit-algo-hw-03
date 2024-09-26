from datetime import datetime
import re

def get_days_from_today(date):
    # Создание переменной для случая неверного выполнения программы 
    when_date_is_not_correct = "The data is not correct, the date must be in the following format: 'YYYY-MM-DD'"
    # Создание паттерна для проверки подходит ли строка под необходимый формат даты
    pattern = r"\d{4}-\d{2}-\d{2}"
    # Сам поиск паттерна в строке date
    match = re.search(pattern, date)
    # проверю что вернул match, еси он не None тоспрограммы работает дальше 
    if match:
        # проверка исключений, если месяц или день в date не соответствуют верным значениям 
        try:
            #Находим сегоднешнюю дату
            now = datetime.today()
            # Преабразовываем строку date в объект datetime
            delta_date = datetime.strptime(date, '%Y-%m-%d')
            return delta_date.toordinal() - now.toordinal()
        except ValueError:
            return when_date_is_not_correct
    else:
        return when_date_is_not_correct

# Тестовые запуски
# print(get_days_from_today('2024-09-23'))
# print(get_days_from_today('2024.09.23'))
# print(get_days_from_today('2024-13-23'))
# print(get_days_from_today('2024-09-31'))

