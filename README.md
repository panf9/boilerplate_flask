# PASOS PARA CREAR UN PROYECTO EN FLASK

1. Creamos el proyecto e instalamos un entorno virtual

```{python}
python -m venv venv
```

## Creamos un archivo principal

```{python}
touch main.py
```

## Creamos una carpeta app

dentro de nuestro proyecto creamos una carpeta app

```{python}
mkdir app
```

Nuestro proyecto debe de tener la siguiente estructura

```
|-Proyecto
    |-venv
    |-app
        |-__init__.py
        |-config
            |-__init__.py
        |-models
            |-__init__.py
            |-role_models.py
    |-.env
    |-main.py
    |-requirement.txt
    |-README.md

```

## Instalando paquetes

### Flask

```{python}
pip install flask
```

### Autopep8

```{python}
pip install autopep8
```

### python-dotenv

```{python}
pip install python-dotenv
```

### Flask-SQLAlchemy

```{python}
pip install Flask-SQLAlchemy
```

[Doc SQLAlchemy](https://docs.sqlalchemy.org/en/20/dialects/)

[Configuración de SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/#configure-the-extension)

### Psycopg2

```{python}
pip install psycopg2-binary
```
