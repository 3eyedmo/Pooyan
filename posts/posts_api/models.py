import mongoengine as me
from datetime import datetime
from jwt_helper.models import User


class Post(me.Document):
    title = me.StringField()
    created = me.DateTimeField(default=datetime.now)
    like_numbers = me.IntField(default=0)
    author = me.EmbeddedDocumentField(User)
