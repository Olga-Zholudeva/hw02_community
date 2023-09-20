# backend_community_homework

[![CI](https://github.com/yandex-praktikum/hw02_community/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/yandex-praktikum/hw02_community/actions/workflows/python-app.yml)

## Добавляем новые опции в [социальную сеть Yatube](https://github.com/Olga-Zholudeva/yatube_project)

## Суть проекта:

- на главную страницу выводятся десять последних записей
- в админ-зоне доступно управление объектами модели Post: можно публиковать новые записи или редактировать/удалять существующие
- Пользователь может перейти на страницу любого сообщества, где отображаются десять последних публикаций из этой группы

### Технологии
- Python 3.7
- Django 2.2.19

### Запуск проекта:

- Клонируем репозиторий: **git clone [hw02_community](https://github.com/Olga-Zholudeva/hw02_community)**
- Cоздаем и активировируем виртуальное окружение: **python3 -m venv env source env/bin/activate**
- Устанавливаем зависимости из файла requirements.txt: **pip install -r requirements.txt**
- Переходим в папку yatube: **cd yatube**
- Применяем миграции: **python manage.py makemigrations**
- Создаем супер пользователя: **python manage.py createsuperuser**
- Применяем статику: **python manage.py collectstatic**
- В папку с проектом, где файл settings.py добавляем файл .env куда прописываем наши параметры:
  - SECRET_KEY='Ваш секретный ключ'
  - ALLOWED_HOSTS='127.0.0.1, localhost'
  - DEBUG=True
- Запускаем проект на локальном устройстве **python3 manage.py runserver**

### Проект выполнила:

**Ольга Жолудева**



