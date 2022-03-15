import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'Curso.sqlite3')
    }
}
POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Curso',
        'USER': 'postgres',
        'PASSWORD': '1904',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Curso',
        'USER': 'root',
        'PASSWORD': 'David1904',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}