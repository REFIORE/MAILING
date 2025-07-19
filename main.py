from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


message = MIMEMultipart()

message['From'] = 'REFIORE@yandex.ru'
message['To'] = 'REFIORE@yandex.ru'
message['Subject'] = 'Это твоя рассылка'

modules_completed = [
    'Командная строка',
    'Git и GitHub',
    'Основы Python',
    'WEB разработка (HTML / CSS)',
    'API веб-сервисов',
]

executable_modules = [
    'Знакомство с Django: ORM',
    'Вёрстка для питониста',
    'Продвинутая вёрстка Html/Css',
]

time_of_study = '3 года'


if modules_completed:
    text_completed = f'''Привет Мама(Папа),
    я занимаюсь в школе третье место уже {time_of_study}.
    В процессе я выполнил модули: {modules_completed}!
    Сейчас я работаю над модулями {executable_modules}.
    Обучение мне нравится, я получил море знаний!'''
else:
    text_completed = f'''Привет Мама(Папа),
    я занимаюсь в школе третье место уже {time_of_study}.
    Сейчас я работаю над модулями {executable_modules}.
    Пока что я улучшаю свои навыки и узнаю много нового!'''


message.attach(MIMEText(text_completed, 'plain'))

password = 'qawrzrykcgficefa'


server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login('REFIORE@yandex.ru', password)
server.sendmail('REFIORE@yandex.ru', 'REFIORE@yandex.ru', message.as_string())
server.quit()
