import mongoengine as me
from django.utils import timezone
from accounts.utils.hasher import hasher

class User(me.Document):
    username = me.StringField()
    password = me.StringField()
    created = me.DateTimeField(default=timezone.now)

    @property
    def is_authenticated(self):
        return True

    def set_password(self, password: str):
        self.password = hasher(password)

    def check_password(self, password: str):
        hashed_password = hasher(password)
        return hashed_password == self.password
    


