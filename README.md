### Проект "Doska"
##### Мини-аналог Авито, где пользователи могут размещать товары или свои услуги. Некоммерческий проект.
<img src="https://github.com/dmitry-svechkar/pet_django/assets/138603861/aaefd3d8-af88-4fa3-ab38-ea7404c4345c.jpg" width="200" height="100" />

##### Стек технологий
<div>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="50" height="50">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/django/django-plain.svg" width="50" height="50">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg" width="50" height="50">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg" width="50" height="50">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original-wordmark.svg" width="50" height="50">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg" width="50" height="50">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/redis/redis-original.svg" width="50" height="50">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original.svg" width="50" height="50">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/nginx/nginx-original.svg" width="50" height="50">
<img src="https://github.com/dmitry-svechkar/Doska-django-project/assets/138603861/cdfcbedb-f605-4ab2-91ce-41cc450d7bf1" width="80" height="50">
</div>

###### Что сделано в проекте:
- Подключен и настроен двухфакторный механизм регистрации на базе django-registration c потверждением почты и активации учетной записи. Настроен SMTP. ✅
- Написаны кастоный UserManager и модель пользователя.✅ 
- Реализован кастомный бекенд для авторизации на сайте посредством почты или логина (по выбору пользователя) ✅
- Переработана часть frontend под реализованную функциональность. ✅
- Реализована сущность создания и добавления товаров. Товар проходит модерацию, после чего публикуется на площадке. ✅ 
- Добавлена возможность одновременного добавления 2 и более фотографий к товару. ✅
- Реализован функционал по добавлению товаров в список желаемых покупок. ✅
- Реализована логика добавления товаров в корзину с калькуляцией суммы покупок и кол-вом товаров. ✅
- Подключена PostgreSQL. ✅
- Подключен Kolo для отладки бекенда и оптимизации запросов. ✅
- Проект покрыт тестами и продолжает покрываться по мере появления новой функциональности. ✅
- Подключение Redis для кешировашия списка товаров и избранного. ✅
- Подключение Redis как брокер сообщений. ✅
- Настроена админ-панели. ✅
- Подключение планировщика задач (Celery) ✅
  - Задачи по отправке email при регистрации.
  - При оформлении заказа отправляется 2 письма: 1 - покупателю с составом заказа. 2 - продавцу c заявкой заказа. 
  - Задачи при блокировке модератором обявления за нарушения/ размещения объявления/ потверждения и 'выпуск' на сайт.
  - При создании пользователя с ролью 'модератор' 1 раз в 60 минут автоматически направляется напоминание о необхожимости модерировать объявления.(необходимо добавить модератора с правами)

##### Отдельная благодарочка ребятам с BootstrapТема за возможность использовать фронтенд. 🙏

##### Чтобы запустить проект на локальной машине:
###### Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:dmitry-svechkar/Doska-django-project.git
```
###### Перейти в директорию:
```
cd Doska-django-project/infra/
```
###### Создать в директории table файл .env c указанием переменных.
###### при DEBUG = True, sqlite3

```
# django settings
SECRET_KEY=any_secret_key_of_django_project

DEBUG=False
CSRF_TRUSTED_ORIGINS =http://domain:port
CORS_ORIGIN_WHITELIST =http://domain:port
>>>>>>> dev

# db settings
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
#redis
LOCATION=redis://adress:6379

```
###### Поднять контейнеры
```
docker-compose up
```

###### Выполнить миграции, собрать и копировать статистику:
```
docker exec web python manage.py migrate
docker exec web python manage.py collectstatic
docker exec web cp -r /collected_static/. /app/static/
```
###### Создать суперпользователя:
```
python manage.py сreatesuperuser
```
###### Проект будет доступен по
```
http://localhost:8080
```
###### К проекту подключен dashbord flower для celery
```
http://localhost:5555
```
          
          
