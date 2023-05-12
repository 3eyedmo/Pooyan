import mongoengine as me
from jwt_helper.models import User
from datetime import datetime


class Like(me.Document):
    post_id = me.StringField()
    user = me.EmbeddedDocumentField(User)
    created = me.DateTimeField(default=datetime.now)

