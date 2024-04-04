### Проект "Doska"
##### Мини-аналог Авито, где пользователи могут размещать товары или свои услуги. Некоммерческий проект.
<img src="https://github.com/dmitry-svechkar/pet_django/assets/138603861/aaefd3d8-af88-4fa3-ab38-ea7404c4345c.jpg" width="200" height="100" />

###### Что сделано в проекте:
- Подключен и настроен двухфакторный механизм регистрации на базе django-registration c потверждением почты и активации учетной записи. Настроен SMTP. ✅
- Написаны кастоный UserManager и модель пользователя.✅ 
- Реализован кастомный бекенд для авторизации на сайте посредством почты или логина (по выбору пользователя) ✅
- Переработана часть frontend под реализованную функциональность. ✅
- Реализована сущность создания и добавления товаров. Товар проходит модерацию, после чего публикуется на площадке. ✅ 
- Добавлена возможность одновременного добавления 2 и более фотографий к товару. ✅
- Реализован функционал по добавлению товаров в список желаемых покупок. ✅
- Реализована логика добавления товаров в корзину с калькуляцией суммы покупок и кол-вом товаров.
- Подключена PostgreSQL. ✅
- Подключен Kolo для отладки бекенда и оптимизации запросов. ✅
- Проект покрыт тестами и продолжает покрываться по мере появления новой функциональности. ✅

###### В беклоге 🗓 :
- Настройка админ-панели. 🗒
- Создание функциональностью по модерации объявлений с последующей отправкой письма продавду по статусу или появлению заказу. 🗒
- Подключение Redis 🗒
- Настройка кеширования. 🗒
- Подключение планировщика задач (Celery) 🗒
- Реализация новых фич. 🗒


##### Стек технологий
<div>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="50" height="50">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/django/django-plain.svg" width="50" height="50">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg" width="50" height="50">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg" width="50" height="50">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original-wordmark.svg" width="50" height="50">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg" width="50" height="50">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/redis/redis-original.svg" width="50" height="50">
</div>


##### Отдельная благодарочка ребятам с BootstrapТема за возможность использовать фронтенд. 🙏

##### Чтобы запустить проект на локальной машине:
###### Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:dmitry-svechkar/Doska-django-project.git
```
###### Cоздать и активировать виртуальное окружение:
- Windows
```
python -m venv venv
source venv/Scripts/activate
```
- Linux
```
python3 -m venv venv
source venv/bin/activate
```
###### Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
###### Создать в корневой папке файл .env 
```
SECRET_KEY=any_secret_key_of_django_project
DEBUG=True

# db В прод-среде подключена sqllite3:

POSTGRES_USER=username
POSTGRES_PASSWORD=pass
POSTGRES_DB=name_db
DB_HOST=db
DB_PORT=5432

# Email settings
EMAIL_HOST=smtp.example.com
EMAIL_PORT=Номер порта(int)
EMAIL_HOST_USER=Host-user
EMAIL_HOST_PASSWORD=Host-pass
EMAIL_USE_TLS=0
EMAIL_USE_SSL=1
DEFAULT_FROM_EMAIL=Host-user
ACCOUNT_ACTIVATION_DAYS=1
AUTH_USER_EMAIL_UNIQUE=1
```
###### Выполнить миграции:
```
python manage.py migrate
```
###### Создать суперпользователя:
```
python manage.py сreatesuperuser
```
###### Создать суперпользователя:
```
python manage.py сreatesuperuser
```
###### Запустить проект:

```
python manage.py runserver
```
          
          
