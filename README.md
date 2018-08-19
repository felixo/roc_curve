# roc_curve
Тестовый проект - построение ROC кривой.

## Описание
Данный проект предназначен для построения рок кривой.
Действующий прототип можно посмотреть по ссылке:
http://138.201.116.120:8989/

Можно собрать самостоятельно.

## Installing 
В терминале: 
```console
user@ubuntu$ git clone https://github.com/felixo/roc_curve
```
В вашей папке с виртуальными окрежениями (env) создайте новое с использованием python-3:
```console
user@ubuntu$ virtualenv -p python3 roc_curve
```
Аквтивируйте его:
```console
user@ubuntu$ source roc_curve/bin/activate
```
Перейдите в папку проекта /your/path/roc_curve и установите необходимые зависимости:
```console
user@ubuntu$ pip3 install -r requirements.txt
```
Перейдите в папку roc_curve /your/path/roc_curve/roc_curve и создайте там файл локальных настроек и папку под график:
```console
user@ubuntu$ touch local_settings.py
user@ubuntu$ mkdir media
```
Файл должен выглядеть например так:
```python
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



KEY = 'ew_e3ale$&)8+qgui3eiwno8*%(mvmy3#+t+b$^e8nl*(hr6kq'

DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
Вернитесь в корень проекта /your/path/roc_curve и выполните миграцию:
```console
user@ubuntu$ python manage.py migrate
```
Проект готов, запустите его:
```console
user@ubuntu$ python manage.py runserver
```
Откройте браузер и перейдите по ссылке: http://127.0.0.1:8000/
Загрузите features.npy и person_id.npy через форму и нажмите загрузить файлы. На выходе будет график ROC.

Загрузите features.npy
