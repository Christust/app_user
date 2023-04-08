Agregamos nuestra app a la lista de apps instaladas en settings:
```
INSTALLED_APPS = [
    ...,
    "apps.users",
]
```

Agremos a nuestro settings.py la variable de entorno "AUTH_USER_MODEL" con el valor del modelo de nuestra app que manejara el usuario, antepuesto por el nombre de su app:
```
AUTH_USER_MODEL = "users.User"
```

Ahora podremos correr las migraciones:
```
python manage.py makemigrations
python manage.py migrate
```