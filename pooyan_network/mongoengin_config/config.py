from mongoengine import connect
from django.conf import settings
def config():
    connect(settings.MONGO_CLIENT)