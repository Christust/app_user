from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Se debe indicar la carpeta contenedora si es que existe, en caso de que no dejar solo users.
    name = '<carpeta_contenedora>.users'
