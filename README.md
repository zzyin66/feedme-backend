# feedme-backend

## Migrations

Migrations must be made after altering Models in project files

Go to the project directory

```bash
  cd feedme-backend
```

Make migrations

```bash
  python manage.py makemigrations feedme
  ||
  python3 manage.py makemigrations feedme
```

Migrate

```bash
  python manage.py migrate
  ||
  python3 manage.py migrate
```

## Database

To integrate django with mysql, please make sure to have mysql installed

```bash
  pip install mysqlclient
```

```bash
  Edit the database settings in
  feedme-backend/server/server/settings.py
  
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
  }

```

