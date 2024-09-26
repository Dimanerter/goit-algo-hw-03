from datetime import datetime
import re
import random

#---------------------------Перше завдання-------------------------------------

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

#---------------------------Друге завдання-------------------------------------

def get_numbers_ticket(min, max, quantity):
    # Создание пустого списка для значений
    lottery_ticket = []
    # Проверка условий 
    if min >= 1 and max <= 1000 and min <= quantity <= max:
       # Создание цикла для заполнения списка всеми возможными числами
        while min < max:
            lottery_ticket.append(min)
            min += 1
        # Заполнение нашего списка случайными элементами между min и max без повторений
        lottery_ticket = random.sample(lottery_ticket, quantity)
        lottery_ticket.sort()

    return lottery_ticket
# Тестовые запуски
# print(get_numbers_ticket(1, 100, 6))
# print(get_numbers_ticket(-1, 10000, 6))
# print(get_numbers_ticket(90, 100, 6))

#---------------------------Третє завдання-------------------------------------

def normalize_phone(phone_number):
    pattern = r"[^\d\+]"
    replacement  = ""
    phone_number = re.sub(pattern, replacement, phone_number)

    pattern = r"\+38"
    match = re.search(pattern, phone_number)
    if match == None:
        pattern = r"38"
        match = re.search(pattern, phone_number)
        if match:
            phone_number = "+" + phone_number
        else:
            phone_number = "+38" + phone_number
    
    return phone_number


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

