# feedme-backend

## Installation

Make sure to run in Python virtual environment for backend server

Install Backend Dependencies
```bash
  pip install -r requirements.txt
```

Install Frontend Dependencies
Cd into /frontend
```bash
  npm i
```

To integrate django with mysql, install mysqlclient & mysql server (workbench recommended)

Install mysql client (if somehow not installed by requirements.txt)
```bash
  pip install mysqlclient
```
Install mysql server
```bash
  https://dev.mysql.com/downloads/mysql/
```
Open terminal
```bash
  mysql -u root -p

  CREATE DATABASE feedme;

  SHOW DATABASES;
  +--------------------+
  | Database           |
  +--------------------+
  | feedme             |
  | information_schema |
  | mysql              |
  | performance_schema |
  | sys                |
  +--------------------+
```

Edit the database settings in feedme-backend/server/server/settings.py
```bash
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_mysql_username',
        'PASSWORD': env('MY_DB_PW'),
        'HOST': 'localhost',
        'PORT': '3306',
    }
  }
```
Create a .env file in the same directory as settings.py and add the following line
```bash
  MY_DB_PW=<your_mysql_password>
```
## Running the server
Run the server
```bash
  python manage.py runserver
```

## Running the frontend app
Cd into /frontend
```bash
  npm run dev

## Migrations

Migrations must be made after altering Models in project files

Go to the project directory

```bash
  cd feedme-backend
```

Make migrations

```bash
  python manage.py makemigrations feedme
```

Migrate

```bash
  python manage.py migrate
```
