<h2 align="center">Mars(First Social Network) by Jirniy</h2>

Социальная сеть на Django Rest Framework.

### Инструменты разработки

**Стек:**
- Python >= 3.8
- Django Rest Framework
- Postgres

## Старт

#### 1) Создать образ

    docker-compose build

##### 2) Запустить контейнер

    docker-compose up
    
##### 3) Перейти по адресу

    http://127.0.0.1:8000/api/v1/swagger/

## Разработка с Docker

##### 1) Сделать форк репозитория

##### 2) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 3) В корне проекта создать .env.dev

    DEBUG=1
    SECRET_KEY=fdsadqw3f32wg<43g3hv$%#@%F$F$$F$F
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
    
    # Data Base
    POSTGRES_DB=mfsn
    POSTGRES_ENGINE=django.db.backends.postgresql
    POSTGRES_DATABASE=mfsn
    POSTGRES_USER=mfsn_user
    POSTGRES_PASSWORD=mfsn_pass
    POSTGRES_HOST=mfsn-db
    POSTGRES_PORT=5433
    DATABASE=postgres

    # Email
    DEFAULT_FROM_EMAIL=your@your.com
    EMAIL_USE_TLS=True
    EMAIL_HOST=your_smtp
    EMAIL_HOST_USER=your@your.com
    EMAIL_HOST_PASSWORD=pass
    EMAIL_PORT=587
    
##### 4) Создать образ

    docker-compose build

##### 5) Запустить контейнер

    docker-compose up
    
##### 6) Создать суперюзера

    docker exec -it mfsn_mfsn_back_1 python manage.py createsuperuser
                                                        
##### 7) Если нужно очистить БД

    docker-compose down -v
 
## License

[BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

Copyright (c) 2022-present, Jirniy




