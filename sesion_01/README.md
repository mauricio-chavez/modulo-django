# Sesión 01

## Creación de entorno virtual

Mac y Linux:

```command-line
python3 -m venv <nombre_del_entorno>
```

Windows:

```command-line
python -m venv <nombre_del_entorno>
```

## Activar entorno virtual

Mac y Linux:

```command-line
source <nombre_del_entorno>/bin/activate
```

Windows:

```command-line
<nombre_del_entorno>\Scripts\activate
```

## Desactivar

```command-line
deactivate
```

## Poner dependencias de proyecto en requirements.txt

```command-line
pip freeze > requirements.txt
```

## Instalar dependencias de requirements.txt (cuando no están instaladas)

```command-line
pip install -r requirements.txt
```

## Comenzar projecto con Django

```command-line
django-admin startproject <nombre_del_proyecto> .
```

## Correr servidor

```command-line
python manage.py runserver
```

## Crear una nueva app

Las siguientes formas hacen lo mismo:

```command-line
django-admin startapp <nombre_del_app>
```

```command-line
python manage.py startapp <nombre_del_app>
```

> Cualquier duda mándame un correo a [mauriciochavezolea@gmail.com](mailto:mauriciochavezolea@gmail.com)
