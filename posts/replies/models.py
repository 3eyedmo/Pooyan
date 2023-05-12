from comments.models import BaseComment
from mongoengine import StringField


class Reply(BaseComment):
    comment_id = StringField()