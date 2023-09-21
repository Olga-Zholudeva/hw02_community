# backend_community_homework

## Добавляем новые опции в [социальную сеть Yatube](https://github.com/Olga-Zholudeva/yatube_project)

## Суть проекта:

- На главную страницу выводятся десять последних записей
- В админ-зоне доступно управление объектами модели Post: можно публиковать новые записи или редактировать/удалять существующие
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
- Запускаем проект на локальном устройстве: **python3 manage.py runserver**

### Проект выполнила:

 **Ольга Жолудева**



