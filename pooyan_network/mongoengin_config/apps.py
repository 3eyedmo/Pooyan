from django.apps import AppConfig
from mongoengin_config.config import config

class MongoenginConfigConfig(AppConfig):
    config()
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mongoengin_config'
