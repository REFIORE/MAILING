from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

message = MIMEMultipart()

message['From'] = 'aras_andrey@bk.ru'
message['To'] = 'aras.refiore@gmail.com'
message['Subject'] = 'Это твоя рассылка\nThis your mailing'

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

text_completed = f'''Привет Мама(Папа),
        я занимаюсь в школе третье место уже {time_of_study}.
        В процессе я выполнил модули: {modules_completed}!
        Сейчас я работаю над модулями {executable_modules}.
        Обучение мне нравится, я получил море знаний!'''

text_uncompleted = f'''Привет Мама(Папа),
        я занимаюсь в школе третье место уже {time_of_study}.
        Сейчас я работаю над модулями {executable_modules}.
        Пока что я улучшаю свои навыки и узнаю много нового!'''


def text_output():
    if modules_completed:
        print(text_completed)
    else:
        print(text_uncompleted)


message.attach(MIMEText(text_output(), "plain"))
