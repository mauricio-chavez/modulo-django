# Cambio de base de datos

## Docker

```command-line
docker pull postgres
docker run --name <nombre-del-contenedor> -p 5432:5432 -e POSTGRES_PASSWORD=<contraseña_postgres> -d postgres
```

## Python

```command-line
pip install psycopg2
```

En `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '<contraseña_postgres>',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
