import mongoengine as me
from jwt_helper.models import User
from datetime import datetime

class BaseComment(me.Document):
    text = me.StringField()
    user = me.EmbeddedDocumentField(User)
    created = me.DateTimeField(default=datetime.now)

    meta = {'allow_inheritance': True}

class Comment(BaseComment):
    post_id = me.StringField()
