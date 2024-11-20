import os
from dotenv import load_dotenv
from weather_sdk import get_new_event, SMSServer


load_dotenv()

forecast_token = os.getenv('FORECAST_TOKEN')
town_title = 'Курск'
print(f'forecast_token: {forecast_token}')

token = os.getenv('SMS_TOKEN')
server = SMSServer(token)
print(f'sms_token: {token}')
print(f'server: {server}')

new_event = get_new_event(forecast_token, town_title)
event_date = new_event.get_date()
event_time = new_event.get_time()
event_area = new_event.get_area()
phenomenon_description = new_event.get_phenomenon()

sms_template = '''{town_title}: {event_time} {event_date} {event_area} ожидается {phenomenon_description}. Будьте внимательны и осторожны.'''

print(f'token: {token}')
print(f'new_event: {new_event}')
print(f'phenomenon_description: {phenomenon_description}')
print(f'town_title: {town_title}')
print(f'event_time: {event_time}')
print(f'event_date: {event_date}')
print(f'event_area: {event_area}')

sms_message = sms_template.format(
    phenomenon_description = phenomenon_description,
    town_title = town_title,
    event_time = event_time,
    event_date = event_date,
    event_area = event_area,
)

server.send(sms_message)

# Гипотеза 1: В переменной нет прогноза погоды для Курска
# Способ проверки: Выведу переменную new_event
# Код для проверки: print(f'new_event: {new_event}')
# Установленный факт: выводит "Регион:  Погода:"
# Вывод: Гипотеза подтвердилась. new_event не содержит необходимой информации

# Гипотеза 2.1: town_title на самом деле пуста
# Способ проверки: Выведу переменную town_title
# Код для проверки: print(f'town_title: {town_title}')
# Установленный факт: выводит "Курск"
# Вывод: Гипотеза не подтвердилась

# Гипотеза 2.2: В town_title не название города
# Способ проверки: Выведу переменную town_title
# Код для проверки: print(f'town_title: {town_title}')
# Установленный факт: выводит "Курск"
# Вывод: Гипотеза не подтвердилась

# Гипотеза 3.1: token от погодного сервиса пуст
# Способ проверки: Выведу переменную token
# Код для проверки: print(f'forecast_token: {token}')
# Установленный факт: выводит "None"
# Вывод: Гипотеза подтвердилась

# Гипотеза 3.2: token от СМС-сервиса пуст
# Способ проверки: Выведу переменную token
# Код для проверки: print(f'sms_token: {token}')
# Установленный факт: выводит "None"
# Вывод: Гипотеза подтвердилась

# Гипотеза 4.1: Может, `token` всё ещё пуст?
# Способ проверки: Выведу переменную token
# Код для проверки: print(f'token: {token}')
# Установленный факт: token: aGVsbG8gY3J5cHRvIGVudHVzaWFzdCA7KQ==
# Вывод: Гипотеза не подтвердилась

# Гипотеза 4.2: Может, в токене не то значение, не `85b98d96709fd49a69ba8165676e4592`?
# Способ проверки: Выведу переменную token
# Код для проверки: print(f'token: {token}')
# Установленный факт: token: aGVsbG8gY3J5cHRvIGVudHVzaWFzdCA7KQ==
# Вывод: Гипотеза подтвердилась

# Гипотеза 4.3: Может, значение `85b98d96709fd49a69ba8165676e4592` успевает измениться до строчки `new_event = ...`?
# Способ проверки: Выведу переменную token сразу после присвоения ей первого токена
# Код для проверки: print(f'forecast_token: {token}')
# Установленный факт: forecast_token: 85b98d96709fd49a69ba8165676e4592
# Вывод: Гипотеза подтвердилась. Переменная token меняется после переприсвоения ей второго значения

# Гипотеза 5.1: Переменная `event_time` пуста/в ней не время
# Способ проверки: Выведу переменную
# Код для проверки: print(f'event_time: {event_time}')
# Установленный факт: Выводит "ночью"
# Вывод: Гипотеза не подтвердилась

# Гипотеза 5.2: Переменная `event_date` пуста/в ней не дата
# Способ проверки: Выведу переменную
# Код для проверки: print(f'event_date: {event_date}')
# Установленный факт: Выводит "24 ноября"
# Вывод: Гипотеза не подтвердилась

# Гипотеза 5.3: Переменная `event_area` пуста/в ней не место
# Способ проверки: Выведу переменную
# Код для проверки: print(f'event_area: {event_area}')
# Установленный факт: Выводит "клх Калач-на-Дону"
# Вывод: Гипотеза не подтвердилась

# Гипотеза 5.4: Переменная `phenomenon_description` пуста/в ней не описание погодного явления
# Способ проверки: Выведу переменную
# Код для проверки: print(f'phenomenon_description: {phenomenon_description}')
# Установленный факт: Выводит "ледяной дождь"
# Вывод: Гипотеза не подтвердилась

# Гипотеза 6: Переменная sms_template содержит опечатки в названиях переменных
# Способ проверки: Выделить проверяемую переменную и проверить выделилась ли она во всех местах
#       где она используется, а также скопирую и вставлю названия переменных в переменную sms_template
# Код для проверки: ...
# Установленный факт: Везде переменные совпадают
# Вывод: Гипотеза не подтвердилась

# Гипотеза 7: Проверить .format() поддерживает представленное в скрипте форматирование
# Способ проверки: Проверю запись .format() в sms_template и, при необходимости, скорректирую
# Код для проверки: ''''{town_title}:'''.format(town_title = town_title)
# Установленный факт: Скорректированный формат решил проблему
# Вывод: Гипотеза подтвердилась